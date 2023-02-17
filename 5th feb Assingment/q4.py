# Q4. Why self is used in OOPs? inpython
# In Python, self is a special parameter that is used in object-oriented programming (OOP) to refer to the instance of the class that the method is being called on. It is a convention in Python to use self as the name of the first parameter in instance methods.

# The self parameter allows instance methods to access and modify the instance variables of the object. When you call an instance method on an object, Python automatically passes a reference to the object as the self parameter. This allows the method to access and modify the object's attributes.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

# Creating an object of class Person
person = Person("ghfgfd", 25)

# Calling the introduce method on the object
person.introduce()  # Output: My name is Alice and I am 25 years old.
# In this example, we define a Person class with an __init__() method that takes two parameters - name and age. Inside the method, we use these parameters to set the name and age instance variables of the object.

# We then define an introduce() method that takes only the self parameter. Inside the method, we use the self parameter to access the object's name and age instance variables and print them.

# When we create an object of the Person class and call the introduce() method on it, Python automatically passes a reference to the object as the self parameter. This allows the method to access and print the object's name and age attributes.

# In summary, the self parameter is used in Python to refer to the instance of the class that the method is being called on. It allows instance methods to access and modify the object's attributes, and is a convention in Python to use self as the name of the first parameter in instance methods.