# Write a python program to print Python Exception Hierarchy.

def print_exception_hierarchy(exception_class, depth=0):
    print("    " * depth + exception_class.__name__)
    for subclass in exception_class.__subclasses__():
        print_exception_hierarchy(subclass, depth+1)

print_exception_hierarchy(BaseException)

