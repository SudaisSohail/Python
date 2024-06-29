# Those functions who takes a function as argument or returns a function are called "higher-order functions"

import functools as func

lst = [1, 2, 5, 9, 12, 4, 7, 10, 3, 6, 8, 11, 15, 18, 19, 13, 14, 16, 17, 20, 0]
lst.sort()

# Reduce -> Reduces an iterable into a single value
reduced_list = func.reduce(lambda x, y : x + y, lst, 10000) #(callable, iterable, initial: starts from this and then continues with iterable)
print(reduced_list)

# Total_ordering -> It automatically creates comparision operators for our class if we define "==" and (">" or "<" or ">=" or "<=")
# Defined only __eq__ and __lt__ and it is not giving error when other comparision operators are called

@func.total_ordering
class Car:
    def __init__(self, company, mileage):
        self.company = company 
        self.mileage = mileage

    def __eq__(self, other):
        return self.mileage == other.mileage and self.company == other.company

    def __lt__(self, other):
        return self.mileage < other.mileage

c1 = Car("BMW", 1000)
c2 = Car("Ferrari", 1800)

print(c1 == c2)
print(c1 < c2)
print(c1 > c2)
print(c1 <= c2)
print(c1 >= c2)

# Partial

def multiply(a, b):
    return a * b

def multiply_10(a):
    return multiply(a, 10)

print(multiply_10(100))

# The multiply_10 function is equivalent to the following:

multiply_ten = func.partial(multiply, 10)   # Takes in a callable and arguments for that function
print(multiply_ten(100))

# Wraps --> Decorates a function inside the decorator function

def decorator(function):
    
    #@func.wraps(function)
    def wrapper(*args, **kwargs):
        print(f"{function.__name__} ran")
        return function(*args, **kwargs)
    return wrapper

@decorator
def add(a, b):
    """documentation strings of function 'add'"""
    return a + b

print("\n")
print(add(1, 2))
print(add.__name__) # printing wrapper
print(add.__doc__)  # printing None because wrapper have no doc strings

def decorators(function):
    
    @func.wraps(function)
    def wrapper(*args, **kwargs):
        print(f"{function.__name__} ran")
        return function(*args, **kwargs)
    return wrapper

@decorators
def addition(a, b):
    """documentation strings of function 'add'"""
    return a + b

print("\n")
print(addition(1, 2))
print(addition.__name__) # printing addition
print(addition.__doc__)  # printing actual doc-strings

# singledispatch --> Decorated a function to make it a generic function

print("\nSingledispatch")

def append_one(obj):
    if type(obj) == list:
        return obj.append(1)
    elif type(obj) == set:
        return obj.union({1})
    elif type(obj) == str:
        return obj + "1"
    else:
        print(f"Unsupported type {type(obj)}")

@func.singledispatch
def append_1(obj):          # It is executed if the requirement does not meet in its own functions
    return f"Unsupported type {type(obj)}"

@append_1.register(list)
def _(obj):
    return obj + [1]

@append_1.register(set)
def _(obj): 
    return obj.union({1})

@append_1.register(str)
def _(obj):  
    return obj + "1"

print(append_1(100))









"""# cached_property

class Marksheet:
    def __init__(self, *grades):
        self.grades = grades

    @func.cached_property
    def total(self):
        print("Calculating total...")
        return sum(self.grades)

    @func.chached_property
    def average(self):
        print("Calculating average...")
        return self.total / len(self.grades)

m = Marksheet(100, 90, 95)

m.total"""



