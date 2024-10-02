import requests_cache
import requests
from typing import List

# Initialize the cache session
session = requests_cache.CachedSession("tfl_cache")


class TFLApi:
    BASE_URL = "https://api.tfl.gov.uk/"

    def __init__(self):
        self.header = {"content-type": "application/json"}

    def get(self, endpoint: str, expire_after: int) -> List[dict]:
        try:
            response = session.get(
                f"{self.BASE_URL}/{endpoint}", expire_after=expire_after
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {endpoint}: {e}")
            return []

    def get_lines(self) -> List[dict]:
        return self.get("Line/Route", expire_after=86400)

    def get_disruptions(self) -> List[dict]:
        return self.get("Line/Mode/tube/Disruption", expire_after=600)

    def get_stations(self) -> List[dict]:
        return self.get("StopPoint/Mode/tube", expire_after=86400)
