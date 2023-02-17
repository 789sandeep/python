# Q5. What is inheritance? Give an example for each type of inheritance.
# inheritance is a fundamental concept in object-oriented programming (OOP) that allows a new class to be based on an existing class, inheriting its attributes and methods. The existing class is called the parent class or superclass, and the new class is called the child class or subclass. Inheritance allows code reuse, promotes code organization, and provides a way to create specialized classes from more general ones.

# There are four types of inheritance:

# Single Inheritance: In single inheritance, a subclass inherits the attributes and methods of a single parent class.

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return "Woof!"

# Creating an object of class Dog
my_dog = Dog("Buddy")

# Accessing the name attribute and calling the speak method on the object
print(my_dog.name)    # Output: Buddy
print(my_dog.speak()) # Output: Woof!

# In this example, we define a Animal class with an __init__() method that takes a name parameter, and a speak() method that raises a NotImplementedError. We then define a Dog class that inherits from the Animal class, and overrides the speak() method to return "Woof!".

# Multiple Inheritance: In multiple inheritance, a subclass inherits the attributes and methods of multiple parent classes.

class Vehicle:
    def __init__(self, color):
        self.color = color

class Engine:
    def start(self):
        return "Engine started."

class Car(Vehicle, Engine):
    def __init__(self, make, model, color):
        Vehicle.__init__(self, color)
        self.make = make
        self.model = model

# Creating an object of class Car
my_car = Car("Toyota", "Corolla", "Red")

# Accessing the color attribute and calling the start method on the object
print(my_car.color)  # Output: Red
print(my_car.start()) # Output: Engine started.

# In this example, we define a Vehicle class with an __init__() method that takes a color parameter, an Engine class with a start() method, and a Car class that inherits from both Vehicle and Engine. We then define an __init__() method for the Car class that calls the __init__() method of the Vehicle class and sets the make and model instance variables.

