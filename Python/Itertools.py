import itertools
import random
import operator

# Accumulate --> It will add the current and previous element while iterating
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_list = itertools.accumulate(lst)
print(list(sum_list))

# Chain --> Itertools.chain is equivalent to concatenating lists or sets
lst2 = ["A", "B", "C", "D", "E"]
chain_list = itertools.chain(lst, lst2)
print(list(chain_list))

# Compress --> Returns only those elements whose corresponding value is "True" or "1"
names = ["Ibrahim", "Sarah", "Shifa", "Sudais", "Ali", "Izzah", "Muhammad"]
random.shuffle(names) # Removing after shuffling so that no one gets KATTI with me
values = [1, 1, 0, 1, 1, 0, 1]
comp_list = itertools.compress(names, values)
print(list(comp_list))

# Count --> Keeps on counting from 0 to infinite

counter = itertools.count(start=0, step=10)

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
    
# Cycle --> Loops through the given iterable over and over again

cyclist = itertools.cycle([0, 1, 2, 3])

print(next(cyclist))
print(next(cyclist))
print(next(cyclist))
print(next(cyclist))
print(next(cyclist))
print(next(cyclist))
print(next(cyclist))
print(next(cyclist))
print(next(cyclist))

cyclist = itertools.cycle(("On", "Off"))

print(next(cyclist))
print(next(cyclist))
print(next(cyclist))
print(next(cyclist))
print(next(cyclist))

# Zip_longest --> A normal zip function would end with the shortest iterable but it would end with longest one

x = list(zip(lst, lst2)) # Built-in zip function

print(list(itertools.zip_longest(lst, lst2))) # itertools zip_longest function

repeater = itertools.repeat("IBRAHIM", times=3)  # Repeates the same value endlessly if "times" is not specified

for i in repeater:
    print(i)

# Starmap --> It takessecond argument as a list of tupless

squares = list(itertools.starmap(pow, [(0, 2), (1, 2), (2, 2), (3, 2)]))  # Each item of list is passed to function as arguments
print(squares)

# Combination and Permutation

letters = ["A", "B", "C", "D"]
names = ["Beenish", "Sohail"]

# In both of them, values do not repeat
result_combination = itertools.combinations(letters, 2)  # Returns pair of 2 values where order does not matter
repeated_combination = itertools.combinations_with_replacement(letters, 3)
result_permutation = itertools.permutations(letters, 2)  # Returns pair of 2 values where order matters

print("\nResult Combination")
for item in result_combination:
    print(item)

print("\nCombinations with replacement") 
for item in repeated_combination:
    print(item)

print("\nResult Permutation")
for item in result_permutation:
    print(item)

# Product --> Unlike combinations and permutations, it can repeat values. Rest everything is same

numbers = [0, 1, 2, 3]

product_combination = itertools.product(numbers, repeat=3)

print("\nProduct Combination")
for item in product_combination:
    print(item)

# Islice --> Enables us to slice an iterable

sliced = itertools.islice(range(11), 1, 9, 2)  # args(iterable, Optional[start], stop, Optional[step])
print(list(sliced))

# Filterfalse --> Keeps those items in an iterable who are false according to the condition 

filtered = list(filter(lambda x: x % 2 == 1, lst))  # Returns those who are true according to the condition
print(filtered)

filtered = list(itertools.filterfalse(lambda x: x % 2 == 1, lst))  # Returns those who are false according to the condition
print(filtered)

# Dropwhile --> Filters an iterable untill the first item evaluates to False. After that returns the iterable as it is

tup = (2, 4, 6, 0, 1, 2, 3, 2, 1, 0)

drop_till_true = list(itertools.dropwhile(lambda x: x % 2 == 0, tup))  # (function, iterable)
print(drop_till_true)

# Takewhile --> Returns all the True values in an iterable that had occured before any False value

take_true = list(itertools.takewhile(lambda x: x % 2 == 0, tup))
print(take_true)

# Group by --> We can make groups like the following by their states

def get_state(person):
    return person["State"]

people = [{"Name": "Ibrahim", "City": "Neelum Valley", "State": "Kashmir"},
          {"Name": "Sarah", "City": "Neelum Valley", "State": "Kashmir"},
          {"Name": "Beenish", "City": "Karachi", "State": "Sindh"},
          {"Name": "Sohail", "City": "Karachi", "State": "Sindh"}]

person_group = itertools.groupby(people, get_state)

for key, group in person_group:
    print(key)
    for person in group:
        print(person)

# Tee --> Replicates an iterable

copy1, copy2 = itertools.tee(people)
print(list(copy1))
print(list(copy2))