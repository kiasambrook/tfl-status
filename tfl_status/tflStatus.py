import requests
import json
from .Lines import *

def getStatus():
    response = requests.get("https://api.tfl.gov.uk/Line/piccadilly/Status")
    return response.json()

def getLines():
    response = requests.get("https://api.tfl.gov.uk/Line/Mode/tube/Route")
    data = json.loads(response.text)
    reponseLines = []

    for line in data:
        reponseLines.append(Tube(line['id'], line['name']))

    return reponseLines