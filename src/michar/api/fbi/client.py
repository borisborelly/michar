import os
from typing import Generator

import requests


state_abbrs = [
  "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", 
  "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
  "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
  "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
  "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"
]

PUBLIC_ENDPOINT = "https://api.usa.gov/crime/fbi/cde"

class FBIClient:

    endpoint: str
    session: requests.Session

    def __init__(self, endpoint: str = PUBLIC_ENDPOINT, api_key: str = "") -> None:
        self.endpoint = endpoint
        self.api_key = api_key
        
        if api_key == "":
            env_value = os.environ.get("FBI_API_KEY", None)
            if env_value is None:
                raise EnvironmentError("No API key provided; consider setting FBI_API_KEY")
            self.api_key = env_value
        self.session = requests.Session()
        self.session.params["API_KEY"] = self.api_key

    def get_state_agency_oris(self, state_abbr: str) -> Generator[str, None, None]:
        request_path = f'agency/byStateAbbr/{state_abbr}'
        request_url = f'{self.endpoint}/{request_path}'
        resp = self.session.get(request_url)
        resp.raise_for_status()
        agencies = resp.json()
        for agency in agencies:
            yield agency["ori"]


    def get_all_agency_oris(self) -> Generator[str, None, None]:
        for state in state_abbrs:
            for ori in self.get_state_agency_oris(state):
                yield ori
