# Q1. Explain Class and Object with respect to Object-Oriented Programming. Give a suitable example.

# Object-oriented programming (OOP) is a programming paradigm that revolves around the concept of objects. Objects are entities that combine state (data) and behavior (methods) in a single entity. Classes provide a blueprint or template for creating objects, which define the properties and methods that the object will have.

# A class is a user-defined data type that encapsulates data and functionality. It is essentially a template or blueprint that defines the characteristics and behaviors of a group of objects. In a class, we can define attributes or data members that represent the state of an object, and methods or member functions that define the behavior or functionality of the object.

# An object is an instance of a class, which means that it is a specific realization or instantiation of the class blueprint. It contains data members and member functions that are defined in the class. When an object is created, memory is allocated to store its data members, and the constructor of the class is called to initialize the object with the initial values.

# In OOP, objects interact with each other through their methods, and the behavior of an object is influenced by the behavior of other objects in the system. This allows for modular design and promotes code reuse, making it easier to develop and maintain complex software systems.

# In summary, a class provides a blueprint or template for creating objects with specific characteristics and behaviors, while an object is an instance of a class with its own unique values for the attributes defined in the class. OOP is a powerful programming paradigm that allows for the creation of modular, reusable, and maintainable software systems.

class Car:
    def __init__(self, make, model, color, year):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        
    def start(self):
        return self.make,self.model,self.color,self.year

# Create an object of the Car class
my_car = Car("Toyota", "Camry", "red", 2018)
print(my_car.start())