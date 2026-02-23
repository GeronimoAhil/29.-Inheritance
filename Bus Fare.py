class Vehicle:

    def __init__(self, name):
        self.name = name
    def fare(self, distance, fare):
        Totalfare = distance * fare
        return Totalfare
        

class Totalfare(Vehicle):
    pass

School_bus = Totalfare("Bus Volvo")
print("Total fare is ", School_bus.fare(180,12))