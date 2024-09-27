class Line:
    def __init__(self, id, name, modeName, disruptions = []):
        self.id = id
        self.name = name
        self.modeName = modeName
        self.disruptions = disruptions

    def __str__(self):
        return f"Line(id={self.id}, name={self.name}, modeName={self.modeName}, disruptions={self.disruptions})"

    def __repr__(self):
        return self.__str__()

    def getDisruptions(self):
        return self.disruptions