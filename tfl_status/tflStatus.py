import requests
import json
from .Lines import *
import requests_cache

def getStatus():
    response = requests.get("https://api.tfl.gov.uk/Line/piccadilly/Status")
    return response.json()

def getLines():
    session = requests_cache.CachedSession('tube_lines', expire_after=3600)
    response = session.get("https://api.tfl.gov.uk/Line/Mode/tube/Route")
    data = json.loads(response.text)
    reponseLines = []

    for line in data:
        reponseLines.append(Tube(line['id'], line['name']))

    return reponseLines