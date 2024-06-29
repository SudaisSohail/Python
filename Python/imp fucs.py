from functools import reduce
import time

all_funcs = ["zip", "filter", "map", "reduce", "min", "max", "any", "all", "enumerate", "dir", "help", "quit", "*repr", "*divmod"]

# Zip Function  --> Returns a list of tuples of corresponding elements og three lists provided

names = ["Ibrahim", "Sarah", "Shifa", "Sudais"]
ages = [2, 6, 18, 15]
type_ = ["Boy", "Girl", "Girl", "Boy"]

print(list(zip(names, ages, type_)))

# Map Function  --> Updates all elements in the list using the fuction provided

lst = [1, 2, 5, 9, 12, 4, 7, 10, 3, 6, 8, 11, 15, 18, 19, 13, 14, 16, 17, 20, 0]
lst.sort()

mapped_list = list(map(lambda x : x ** x, lst))
print(mapped_list)

# Filter Function  --> Remove elements in the list that do not satisfy the condition given in the function

filtered_list = list(filter(lambda x : x % 2 == 0, mapped_list))
print(filtered_list)

# Map and Filter Example  --> It first filters all the odd numbers from the "lst" and then cubes the remaining numbers

updated_list = list(map(lambda x : x ** 3, list(filter(lambda y : y % 2 == 0, lst))))
print(updated_list)

# Reduce Function  --> Reduces a sequence into a single value by processing the elements according to the fuction provided

reduced_list = reduce(lambda x, y : x + y, lst)
print(reduced_list)

a = [5, 10, 30, 1]
b = {2, 5, 10, 3, 1, 9}
c = (10, 4, 9, 5, 12)
d = {100 : "Ibrahim", 20 : "Sarah", 3 : "Shifa", 10 : "Izzah"}
e = {"Ibrahim" : 2, "Sarah" : 7, "Sudais" : 15, "Shifa" : 18}
f = [[3, 5], [1, 0], [16, 9], [0, 23], [5, 7]]
g = [(2, "Ibrahim"), (7, "Sarah"), (15, "Sudais"), (18, "Shifa")]
h = [("Ibrahim", 2), ("Sarah", 7), ("Sudais", 15), ("Shifa", 18)]

# Min Function  --> Returns the smallest value in an iterable

print(min(a))
print(min(b))
print(min(c))
print(min(d))
print(min(e))
print(min(f))
print(min(g))
print(min(h))

# Max Function  --> Returns the largest value in an iterable

print(max(a))
print(max(b))
print(max(c))
print(max(d))
print(max(e))
print(max(f))
print(max(g))
print(max(h))

# Any Function  --> Returns True if any element in the iterable is True and returns False if the iterable is empty or equals to 0

string = "Hello World"
lst1 = [1, 2, 3, 4]
lst2 = [False, False, 0]
lst3 = ["", "", True]
tup = ([], [], 0)

print(any(string))
print(any(lst1))
print(any(lst2))
print(any(lst3))
print(any(tup))

# All Function --> Returns True if all the elements in a iterable is true else returns false

print(all(string))
print(all(lst1))
print(all(lst2))
print(all(lst3))
print(all(tup))

# Enumerate Function --> Fetches index and element of the iterable and assigns the value to i and element respectively

for i, element in enumerate(names):
    print(i, element)

# Dir Function  --> Returns all the attributes related to the provided object

print(dir(set)) 

# Help Function  --> Returns a document on the given object

print(help(sum))

# Compile Function --> Interprets the code of the first argument

code = "print('Ibrahim')\ntime.sleep(2)\nprint('Sarah')"
compiled_code = compile(code, "", 'exec')

exec(compiled_code)                             # Does not need to be printed

x = 10
eval_code = compile("x >= 10", "", "eval")
print(eval(eval_code))                         # Need to be printed