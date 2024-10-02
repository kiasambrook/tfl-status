import requests_cache
import os
import requests
from typing import List


# Create cache directory if it doesn't exist
cache_dir = "cache"
os.makedirs(cache_dir, exist_ok=True)

# Initialize the cache session
session = requests_cache.CachedSession(os.path.join(cache_dir, "tfl_cache"))


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

    def get_arrival_predictions(self, station_id: str) -> List[dict]:
        return self.get(f"StopPoint/{station_id}/Arrivals", expire_after=30)
