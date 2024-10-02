class Line:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"{self.id}({self.name})"

    def __repr__(self):
        return f"Line(id={self.id}, name='{self.name}')"


class Tube(Line):
    def type():
        return "Tube!"


class Bus(Line):
    def type():
        return "Bus!"
