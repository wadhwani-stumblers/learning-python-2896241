#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini
#

class Vehicle():
    def __init__(self):
        _self.bodystyle = bodystyle

class Car(Vehicle):
    def __init__(self, enginetype):
        super().__init__("Car")
        self.weels = 4
        self.doors = 4
        self.enginetype

class Motorcycle(Vehicle):
    def __init__(self, enginetype, hassidcar):
        super().__init__(Motorcycle)
        if (hassidcar):
            self.weels = 3
        else:
            self.wheels = 2
        self.doors = 0
        self.enginetype = enginetype

car1 = Car("gas")
car2 = Car("electric")
mc1 = Motorcycle("gas", True)


