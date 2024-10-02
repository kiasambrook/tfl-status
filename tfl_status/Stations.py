from .tflApi import *


class Station:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"{self.id}({self.name})"

    def __repr__(self):
        return f"Station(id={self.id}, name='{self.name}')"

    def set_next_arrivals(self):
        self.next_arrivals = TFLApi().get_arrival_predictions(self.id)

    def get_next_arrivals(self):
        if not hasattr(self, "next_arrivals"):
            self.set_next_arrivals()

        if len(self.next_arrivals) == 0:
            return "No arrivals available"

        return self.next_arrivals

    def get_incidents(self):
        return "No incidents available"
