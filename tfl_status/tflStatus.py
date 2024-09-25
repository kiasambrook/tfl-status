import requests
from nicegui import ui

def getStatus():
    response = requests.get("https://api.tfl.gov.uk/Line/piccadilly/Status")
    return response.status_code