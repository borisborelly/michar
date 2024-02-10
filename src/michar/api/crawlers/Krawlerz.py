from dataclasses import dataclass
import requests
from requests import Response
from michar.api.util import get_logger
import json
from michar.api.profile import ConfigProfile


log = get_logger("crawler")


# @dataclass
# class Krawl(ABC):
#     profile: ConfigProfile = ConfigProfile()
#     source: str = None
#     url: str = None
#     browser: Optional[str] = "Firefox"
#     _driver: RemoteWebDriver = None

#     def __post_init__(self):
#         log.info(f"{self.source=}")
#         self.url = self.profile.get_source_url(self.source)
#         log.debug(f"crawling {self.source=} @ {self.url=}")

#     def shutdown(self):
#         if self._driver:
#             try:
#                 self._driver.close()
#                 self._driver = None
#             except Exception as e:
#                 log.debug(e)

#     @abstractmethod
#     def start_driver(self) -> None:
#         pass

#     def open_page(self, page: str) -> None:
#         self.start_driver()
#         self._driver.get(url=page)
#         log.debug(self._driver)

#     @abstractmethod
#     def crawl(self) -> dict:
#         pass

#     @property
#     def driver(self) -> RemoteWebDriver:
#         return self._driver

#         # def get_div(self, div_id: str):
#         #     """
#         #     gets data from a div name
#         #     """

#         #     # Wait for the dynamic content to load (adjust the timeout as needed)
#         #     div = WebDriverWait(self._driver, 20).until(
#         #         EC.presence_of_element_located((By.ID, div_id))
#         #     )
#         #     ddd = self._driver.find_element_by_id("dropdown_id")
#         #     log.info(div)
#         #     log.info(f"elements {div.find_elements()}")
#         #     return div

#         # def get_element(self, element_id: str) -> WebElement:
#         #     """
#         #     gets data from a dynamic element id
#         #     """
#         #     dynamic_content: WebElement = self._driver.find_element(By.ID, element_id)
#         #     log.info(dynamic_content)
#         #     return dynamic_content

#         # def get_select_div(self, id: str) -> Select:
#         #     return Select(self.get_div(id))

#         # def set_selection_on_div(self, value: str, id: str):
#         # element = self.get_div(id)
#         # entry: Select = Select(element)

#         # entry.select_by_visible_text(value)

#         # log.info(entry)
#         # log.info(element)
#         # return element


# @dataclass
# class RssKrawler(Krawl):
#     def __post_init__(self):
#         return super().__post_init__()

#     def print_rss(self, rss_feed_url: str) -> list:
#         feed: FeedParserDict = feedparser.parse(rss_feed_url)
#         if "entries" in feed:
#             # Iterate over each entry in the feed
#             for entry in feed.entries:
#                 # Print title and link of each entry
#                 print("Title:", entry.title)
#                 print("Link:", entry.link)
#                 print()
#             return feed.entries
#         else:
#             print("No entries found in the feed.")
#             return []


# @dataclass
# class SeleniumKrawler(Krawl):
#     def __post_init__(self):
#         super().__post_init__()
#         log.debug(f"{self._driver=} {self.url}")

#     def start_driver(self):
#         if self.browser == "Firefox":
#             self._driver = webdriver.Firefox()
#             log.info(self.driver)
#         else:
#             log.error("use firefox")

#     def crawl(self) -> dict:
#         return super().crawl()


# @dataclass
# class LbcCrawler(SeleniumKrawler):
#     def __post_init__(self):
#         super().__post_init__()

#     def crawl(self) -> dict:
#         results: dict = {}
#         req: str = "https://longbeach.legistar.com/Calendar.aspx"
#         try:
#             self.open_page(req)
#             # client_id_element = self._driver.find_element_by_xpath(
#             #     "//input[@id='client_id']"
#             # )  # Replace 'some_id' with the actual ID of the input element

#             # print(client_id_element)

#             # for year in [year for year in range(2023, 2024)]:
#             #     # try:
#             #     log.debug(f"Searching {year=}\n{self.url=}")
#             #     # year = str(year)
#             #     # calendar_id: int = self.profile.get_source_field_from(
#             #     #     source=self.source, field=year
#             #     # )
#             #     # log.info(f"{calendar_id=}")
#             #     # req = f"{self.url}"
#             #     # req = self.url.format(calendar_id=calendar_id, year=year)
#             #     req = self.url.format(year=year)
#             #     log.info(f"formatted url FEED is {req=}")

#             #     # self.start_driver()
#             #     # self.open_page(req)

#             #     # # open agenda pdf
#             #     # self.vars["window_handles"] = self.driver.window_handles
#             #     # self.driver.find_element(
#             #     #     By.ID, "ctl00_ContentPlaceHolder1_hypAgenda"
#             #     # ).click()
#             #     # self.vars["win5013"] = self.wait_for_window(2000)
#             #     # self.driver.switch_to.window(self.vars["win5013"])

#         finally:
#             self.shutdown()
#         return results


@dataclass
class LegistarScraper(object):
    url: str = "https://webapi.legistar.com/v1/{client}"
    client: str = None
    headers = {"Accept": "application/json"}

    matters_endpoint: str = "/matters"
    events_endpoint: str = "/events"

    @property
    def api(self) -> str:
        return self.url.format(client=self.client)

    @property
    def matters(self) -> dict:
        return self.query(endpoint=self.matters_endpoint)

    @property
    def events(self) -> dict:
        return self.query(endpoint=self.events_endpoint)

    def query(self, endpoint: str, method: str = "GET", payload: dict = {}) -> dict:
        return self._request(f"{self.api}{endpoint}", method, payload)

    def _request(self, url: str, method: str = "GET", payload: dict = {}) -> dict:
        log.info(f"Request {method=}\n{url=}")
        resp: Response = requests.request(
            method=method, url=url, data=payload, headers=self.headers
        )

        if resp.status_code > 200:
            log.error(f"{url}\n{resp=}")

        log.debug(resp)
        json_resp: dict = resp.json()
        log.info(json.dumps(json_resp, indent=4))
        return json_resp


@dataclass
class LbcCityKrawler(LegistarScraper):
    cache: bool = True

    def __post_init__(self):
        self.client = "LongBeach"

    def crawl(self) -> dict:
        # https://webapi.legistar.com/Home/Examples
        # https://webapi.legistar.com/v1/LongBeach
        # /matters?$filter=year(MatterAgendaDate)%20eq%202023
        # /events?$filter=EventDate+ge+datetime%272014-09-01%27+and+EventDate+lt+datetime%272014-10-01%27
        print("lbc legistar krawl..")
        matters_resp: dict = self.matters
        events_resp: dict = self.events


def get_crawler(source: str) -> LegistarScraper:
    """
    get a crawler for the specified source
    """
    profile: ConfigProfile = ConfigProfile()
    if source == "lbc":
        return LbcCityKrawler()
        # return LbcCrawler(profile=profile, source=source)
    else:
        log.error("add another crawler impl")
