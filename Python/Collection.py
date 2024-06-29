from collections import namedtuple, deque, defaultdict, Counter, ChainMap, OrderedDict

# namedtuple returns a tuple with a named value for each element in the tuple

a = namedtuple("courses", ["name", "technology"])    # First mention the name of tuple and then in a iterable give the name of elements

# Call "a" and then give the values of the names given
s = a("data science", "python")  
s = a._make(["AI", "python"])
print(s)
print(s.name)  # It is like a class and we can access the name or technolgy as (self.name) or (self.technology)
print(s[0])    # We can even access items by index numbers
print(s._asdict()) # Makes a dictionary
print(s._fields) # Returns a tuple of fields
s = s._replace(name = "Machine Learning")  # We can change data but it must be assigned to another variable because tuples are immutable
print(s)
s = s._make(["Tensorflow", "AI"])  # Replace all


# Deque is an optimised list to perform insertion and deletion easily
# If you have provided maxlength, and if the list is full then it will remove the item from the opposite side from where you have appended

languages = ["Java" , "C++" , "C" , "Python" , "JavaScript"]     
d = deque(languages, maxlen=10)
d.append("C#")    # Appending normally i.e to the right side i.e to ending of the list
d.append("PHP")
d.appendleft("Go")  # Appending to the start of the list i.e to the left side
d.pop()   # Popping normally i.e from the right side i.e from ending of the list
d.popleft()    #Popping from the start of the list i.e from the left side
d.extend(["CSS", "HTML", "Delphi"])  # Append many
d.extendleft(["Ruby", "Visual Basic"])  # Appendleft many
print(d)

# Chainmap is a dictionary like class for creating a single view of multiple mappings
# Suppose we have 2 dictionaries and chainmap will convert the dictionaries into an item of a tuple

x = {"a" : "b", "c" : "d"}
y = {"e" : "f", "g" : "h"}

z = ChainMap(x, y)
print(z)

# Counter is a dictionary subclass for counting hashable objects

# Ways to initialize Counter --> Returns a dictionary in which key is the element and the value is element's count
c = Counter("IBRAHIM")
c = Counter(["I", "B", "R", "A", "H", "I", "M"])
c = Counter({"I":2, "B":1, "R":1, "A":1, "H":1, "M":1})
c = Counter(I=2, B=1, R=1, A=1, H=1, M=1)

print(c["I"])  # We can access values of any key like this
print(c["S"])  # "S" is not in "c" so it will simply return "0" instead of raising an error

c.clear()      # Makes the counter object empty

p = [1, 2, 3, 1, 2, 5, 4, 3, 2, 5, 4, 1, 3, 5, 2]
c = Counter(p)   # Returns a dictionary in which key is the element and the value is element's count

print(c)
print(list(c.elements())) # Returns a list of all the all the elements in an order
print(c.items())          # Returns a list of tuples in which first item is the element and the second is its count
print(c.most_common(4))   # Returns a list of tuples of most occured elements in which first item is the element and the second is its count

sub = {1:1, 2:3}  # We can also use a tuple, set or list
c.subtract(sub)  # It subtracts "1" once and element "2" three times from self
print(c)

updated = [1, 1, 4, 4, 4, 4]
c.update(updated)
print(c)

d = Counter([1, 1, 4, 4, 4, 4])
print(c + d)
print(c - d)  # If element count <= 0, it will not be shown in the result

#print(c.total())  # Computes the sum of the counts --> It is in python 3.10

# Ordered Dictionary is dictionary subclass which remembers the order in which the entries were done 

od = OrderedDict()

od[1] = "i"
od[2] = "B"
od[3] = "R"
od[4] = "A"
od[5] = "H"
od[6] = "I"
od[7] = "M"

print((od))
print(od.keys())   # Returns all the keys in the dictionary

od[1] = "I"

print(od)

# Default dictionary is a dictionary subclass which calls a factory function to supply missing values

dd = defaultdict(int)

dd[1] = "Python"
dd[2] = "AI"
dd[3] = "ML"

print(dd[4])

