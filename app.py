import requests
from nicegui import ui

response = requests.get("https://api.tfl.gov.uk/Line/piccadilly/Status")
ui.label("HELLO")
ui.run()