class Station:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"{self.id}({self.name})"

    def getArrivalTimes(self):
        return "No arrival times available"

    def getIncidents(self):
        return "No incidents available"
