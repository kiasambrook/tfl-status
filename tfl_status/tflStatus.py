import requests
import requests_cache
from .Lines import Tube, Bus
from typing import List, Union

# Helper function to get data from the API with caching
def fetch_transport_data(mode: str, cache_name: str, expire_after: int = 3600) -> list:
    session = requests_cache.CachedSession("cache/" + cache_name, expire_after=expire_after)
    try:
        response = session.get(f"https://api.tfl.gov.uk/Line/Mode/{mode}/Route")
        response.raise_for_status()  # Raises an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {mode} lines: {e}")
        return []

# Fetch the status of the Piccadilly line
def get_status() -> dict:
    try:
        response = requests.get("https://api.tfl.gov.uk/Line/piccadilly/Status")
        response.raise_for_status()  # Check for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Piccadilly line status: {e}")
        return {}

# Fetch all lines (tube and bus)
def get_lines() -> List[Union[Tube, Bus]]:
    transport_lines = []

    # Fetch tube lines
    tube_lines = fetch_transport_data('tube', 'tube_lines')
    for line in tube_lines:
        transport_lines.append(Tube(line['id'], line['name']))

    # Fetch bus lines
    bus_lines = fetch_transport_data('bus', 'bus_lines')
    for line in bus_lines:
        transport_lines.append(Bus(line['id'], line['name']))

    return transport_lines
