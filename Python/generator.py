import sys

# Iterator is an object that enables us to loop through a data structure without having to store the values in memory

# Generator is a routine that can be used to control the iteration behaviour of a loop. A generator is very similar to a function that 
# returns an array

# They both are pretty much same thing but generators were introduced in python 3 and use new syntax

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for item in x:
    print(item)    

# The problem in above code is that we have to store each item in our memory which occupies too much space

# Range function is an iterator which creates value each time so we don't need to store it in a data structure

for i in range(1, 11):
    print(i)
    
# Map function is also an iterator or generator that does not store values in memory instead it generates it one at a time
y = map(lambda a : a ** 2, x)
z = list(map(lambda b : b ** 2, x)) 

for j in y:
    print(j)

print(sys.getsizeof(x))              # 136 bytes
print(sys.getsizeof(range(1, 11)))   # 48 bytes
print(sys.getsizeof(y))              # 48 bytes
print(sys.getsizeof(z))              # 152 bytes

# The whole point is that we don't need to store each value in a list, we can generate the value as we loop through it

######################################################  ITERATORS  #########################################################

# A for-loop is calling a special method named "next()" on all of these iterator objects like range(), map() etc. so they give the
# next item of the sequence that we are looping through.

# Calling next function manually; not using for-loop

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

mapped = map(lambda ab : ab ** 2, lst)  
mapped2 = map(lambda ab : ab ** 2, lst2)

print(next(mapped))   # 1
print(next(mapped))   # 4
print(next(mapped))   # 9

print(mapped.__next__())   # 16
print(mapped.__next__())   # 25

print("-----------------")
print("for loop starts")
print("-----------------")

for val in mapped:    # It calls next fuction so it didn't repeat the above 5 values, it continued from 36
    print(val)

# The following while loop is excatly doing what a for loop does

print("\nWhile Loop")

while True:
    try:
        value = next(mapped2)
        print(value)

    except StopIteration:
        print("Done")
        break

# Iter function

it = range(1, 11)
print(it)

#print(next(it))   We can't do this because range function is not an iterator, we have to make "it" an iterator first

it = iter(it)   # Now it is an iterator and next function can work on it

print(next(it))

# Whenever we do this
# "for i in it:"
# For loop automatically calls iter() on it and loops through it using next() even though that object is not an iterator

# This is how we can make our own iterator by using class. It wholly explains how an iterator works

class Iter:

    def __init__(self, n):
        self.n = n
    
    def __iter__(self):
        self.current = -1
        return self

    def __next__(self):
        self.current += 1
        if self.current >= self.n:
            raise StopIteration
        return self.current
        
my_iter = Iter(6)

print("\nMy own iterator running")
for num in my_iter:
    print(num)

########################################################  GENERATOR  ######################################################################

# Generators are only useful when you do not care aboult the data before or after something in an iteration, you only care about the
# current piece of the data that you are looking at. 

def gen(number):
    for i in range(number):
        yield i

# Whenever the "yield" keyword is hit, it pauses the execution of the function and returns this value whatever is iterating through
# this generator object

print("\nGenerators started\n")

generator = gen(6)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

def gen2():
    yield 1  # Pauses the iteration and gives 1
    
    yield 2 
    yield 3
    yield 4
    yield 5

generator2 = gen2()

print("\nGen2 ")

print(generator2.__next__())
print(generator2.__next__())
print(generator2.__next__())
print(generator2.__next__())
print(generator2.__next__())

# We can also do this using for loop as it automatically calls "next()"

def gen3(number):
    for i in range(number):
        yield i

print("\nGen3 started")

for i in gen3(11):
    print(i)

# Generator Comprehension

g_comp = (z for z in range(10))   # Whenever you make a comprehension inside of parentheses, it gives you a generator
print(g_comp)

print(g_comp.__next__())
print(g_comp.__next__())
print(g_comp.__next__())
print(g_comp.__next__())
print(g_comp.__next__())
print(g_comp.__next__())
print(g_comp.__next__())
print(g_comp.__next__())
print(g_comp.__next__())
print(g_comp.__next__())