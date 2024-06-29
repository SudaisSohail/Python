import time
import datetime

# Closures --> A closure had allowed inner_func to have access to message variable which is not inside inner_func

def outer_func(msg):
    message = msg
    
    def inner_func():
        print(message)  # The inner func has access to the free variable which is not local for it(in this case "message")
    return inner_func

hi_func = outer_func("Hi")  # first term function allows us to assign a function to a variable and use that variable as a function
bye_func = outer_func("Bye")

hi_func() # hi_func = outer_func("Hi") outer_func is returning inner_func; that means we have assigned inner_func to hi_func. 
# message is not defined in inner_func but when it is called it still ha saccess to the message variable defined in outer_func. It is being
# called because outer_func is returning it and that return is assigned to hi_func and here hi_func is called means indirectly inner_func
# is called.

bye_func()

# Decorators (functions)

def decorator(org_func):
    def wrapper_func(*args, **kwargs):
        print(f"Wrapper executed this before {org_func.__name__}")
        return org_func(*args, **kwargs)
    return wrapper_func

@decorator    # display = decorator(display)   BOTH ARE EQUAL
def display():
    print("display function ran")

@decorator
def display_info(name, age):
    print(F"My name is {name} and I am {age} years old")

display_info("Ibrahim", 1.7)
display()

# Decorator (classes)

class Dec_class(object):
    def __init__(self, org_func):
        self.org_func = org_func

    def __call__(self, *args, **kwargs):
        print(f"Call method executed this before {self.org_func.__name__}")
        return self.org_func(*args, **kwargs)

@Dec_class    # display = decorator(display)   BOTH ARE EQUAL
def display():
    print("display function ran")

@Dec_class
def display_info(name, age):
    print(F"My name is {name} and I am {age} years old")

print("\n")
display_info("Ibrahim", 1.7)
display()
print("\n")

# Practical Example

def timer(func):  # Calculates the runtime of any function
    def wrapper(*args, **kwargs):
        before = time.time()
        Value = func(*args, **kwargs)
        return f"{Value}   Runtime: {time.time() - before}"
    return wrapper

@timer
def run():
    time.sleep(1)

run()

def log(func):
    def Wrapper(*args, **kwargs):
        with open("logs.txt", "a") as f:
            f.write(f"Called {func.__name__} with ({' '.join([str(arg) for arg in args])}) argument(s) at {datetime.datetime.now()}\n")
        value = func(*args, **kwargs)
        return value
    return Wrapper

@log
@timer
def factorial(num):    # is equivalent to --> 'factorial = log(timer(factorial))'

	if num == 0 or num == 1:

		return 1

	elif num < 0:

		answer = -1

		for n in range(2, -(num) + 1):

			answer *= n

		return answer

	elif num > 0:

		answer = 1

		for n in range(2, num + 1):

			answer *= n

		return answer

print(factorial(1000))
