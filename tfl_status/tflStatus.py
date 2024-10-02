from .Lines import Line
from typing import List, Union
from .tflApi import TFLApi


# Fetch all lines
def get_lines() -> List[Line]:
    api = TFLApi()
    transport_lines = []

    # Fetch lines
    transport_route_response = api.get_lines()
    for line in transport_route_response:
        transport_lines.append(Line(line["id"], line["name"]))

    return transport_lines
