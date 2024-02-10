from dataclasses import dataclass
import requests
from requests import Response
from logging import Logger
from michar.api.util import get_logger
import json
from michar.api.profile import ConfigProfile
from michar.api.sources.legistar import Matter, Event
from datetime import datetime
import base64

start_time: datetime.time = datetime.now()

log: Logger = get_logger("crawler")


@dataclass
class LegistarScraper(object):
    url: str = None
    client: str = None
    headers: dict = None
    filters: dict = None

    def __post_init__(self):
        self.headers = {"Accept": "application/json"}

    matters_endpoint: str = "/matters"
    events_endpoint: str = "/events"

    @property
    def api(self) -> str:
        return self.url.format(client=self.client)

    @property
    def matters(self) -> list[Matter]:
        return self._handle_matters(self.query(endpoint=self.matters_endpoint))

    def _handle_matters(self, data: dict) -> list[Matter]:
        results: list[Matter] = []
        for entry in data.keys():
            # print(key)
            m: Matter = Matter()
            results.append(m)
        return results

    @property
    def events(self) -> dict:
        return self.query(endpoint=self.events_endpoint)

    def _handle_matters(self, data: dict) -> list[Event]:
        results: list[Event] = []
        for key in data.keys():
            # print(key)
            e: Event = Event()
            results.append(e)
        return results

    def _withFilter(self, key: str, value: str):
        log.debug(f"\n{key=},{value=}\n")
        self.filters.update({key: value})
        return self

    def withMatterFilters(self, year: str):
        # /matters?$filter=year(MatterAgendaDate)%20eq%202023
        if year:
            self._withFilter("year(MatterAgendaDate)", year)
        return self

    def withEventFilters(self, starting_date_range: str, ending_date_range: str):
        # /events?$filter=EventDate+ge+datetime%272014-09-01%27+and+EventDate+lt+datetime%272014-10-01%27
        if starting_date_range:
            self._withFilter("EventDate>datetime", starting_date_range)
        elif ending_date_range:
            self._withFilter("EventDate<datetime", ending_date_range)
        return self

    def crawl_matters(self, **kwargs):
        if kwargs.get("year"):
            self.withMatterFilters(kwargs.get("year"))

        return self.matters

    def crawl_events(self, **kwargs) -> dict:
        if kwargs.get("start_time"):
            self.withEventFilters(kwargs.get("start_time"))
        if kwargs.get("end_time"):
            self.withEventFilters(kwargs.get("end_time"))

        return self.events

    def query(self, endpoint: str, method: str = "GET", payload: dict = None) -> dict:
        return self._request(f"{self.api}{endpoint}", method, payload)

    def _apply_filters(self, base_url: str) -> str:
        url_with_filters: str = base_url
        if self.filters:
            log.debug(
                f"\tApplying filters to {base_url}:\n====={json.dumps(self.filters, indent=4)}\n=====\n"
            )

            url_with_filters = f"{base_url}?$filter="
            for key, value in self.filters.items():
                # # TODO base 64 encoding
                # encoded_key = base64.b64encode(key.encode()).decode()
                # encoded_value = base64.b64encode(value.encode()).decode()
                log.debug(key, ":", value)
                url_with_filters = f"{url_with_filters}{key}{value}"
                log.debug(f"{url_with_filters=}")
            log.debug(f"\n*****\nFINAL URL with filters: {url_with_filters}\n*****\n")
        return url_with_filters

    def _request(
        self, endpoint: str, method: str = "GET", payload: dict = None
    ) -> dict:
        log.debug(f"{method=}:{endpoint=}\n{json.dumps(payload, indent=4)}")
        if self.filters:
            endpoint = self._apply_filters(endpoint)

        # TODO add response handling for results > 1000
        # Note that queries replies are limited to 1000 responses.
        # Even with this limit, some calls may return a large amount of data.
        # To make this query more performant:
        # 1) limiting reults to a smaller set of items
        # 2) obtain more items via a second query, use ODATA parameters to page the output like this:
        #       https://webapi.legistar.com/v1/{Client}/matters?$top=10&$skip=0
        #       https://webapi.legistar.com/v1/{Client}/matters?$top=10&$skip=10
        resp: Response = requests.request(
            method=method, url=endpoint, data=payload, headers=self.headers
        )
        log.debug(resp)
        json_resp: dict = resp.json()
        if resp.status_code > 200:
            log.error(f"{endpoint}\n{resp.text}")
        else:
            log.debug(json.dumps(json_resp, indent=4))
        return json_resp


@dataclass
class LBC(LegistarScraper):

    def __post_init__(self):
        self.client = "LongBeach"
        self.url = "https://webapi.legistar.com/v1/{client}"


def get_crawler(source: str) -> LegistarScraper:
    """
    get a crawler for the specified source
    """
    profile: ConfigProfile = ConfigProfile()
    if source.upper() == "LBC":
        return LBC()
    else:
        log.error("add another crawler impl")
