#EX 9

# OOP – Class and Inheritance

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)    
        self.num_doors = num_doors

    def display_info(self):
        print("Make:", self.make)
        print("Model:", self.model)
        print("Number of Doors:", self.num_doors)


car1 = Car("Toyota", "Corolla", 4)
car1.display_info()



"""

Base class Vehicle stores make and model.

Car inherits from Vehicle and adds num_doors.

display_info() prints all details.

"""
