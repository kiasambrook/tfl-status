import requests
import requests_cache
from .Lines import Line
from typing import List, Union

# Helper function to get data from the API with caching
def fetch_transport_data(cache_name: str, expire_after: int = 3600) -> list:
    session = requests_cache.CachedSession("cache/" + cache_name, expire_after=expire_after)
    try:
        response = session.get("https://api.tfl.gov.uk/Line/Route")
        response.raise_for_status()  # Raises an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching lines: {e}")
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

# Fetch all lines
def get_lines() -> List[Union[Line]]:
    transport_lines = []

    linesResponse = fetch_transport_data('transport_lines')
    for line in linesResponse:
        transport_lines.append(Line(line['id'], line['name'], line['modeName'], line['disruptions']))

    return transport_lines

# Fetch all lines of a specific mode
def get_line_by_modeName(lines: List[Union[Line]],modeName: str) -> List[Union[Line]]:
    transport_lines = []

    for line in lines:
        if line.modeName == modeName:
            transport_lines.append(line)

    return transport_lines
