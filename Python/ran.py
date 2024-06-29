import random

data = [15, 40, 93, 4, 82, 100, 35]
colors = ["Red", "Green", "Blue"]
deck = list(range(1, 53))

random.shuffle(data)      # shuffles the elements of the list randomly
print(data)

print(random.random())        # returns a float between 0 and 1 including 0

print(random.randint(0, 100))  # returns an integer between the range provided including upper and lower limit

print(random.randrange(0, 21))  # returns an integer between 0 and 20. It excludes upper limit

print(random.uniform(1, 100))  # returns a float between the range provided excluding upper limit

print(random.choice(data))  # returns a random element from list, tuple or string

results = random.choices(colors, k = 10)  # Randomly picks 10 colours and returns them in a list 
print(results)

results = random.choices(colors, weights = [10, 10, 1], k = 10)  # Picks 10 colours according to their weights and returns them in a list 
print(results)

hand = random.sample(deck, k = 10)  # It is same as choices but it makes always picks unique values

print(random.randbytes(10))         # Returns the given number of characters(literally any character, mostly hexadecimal numbers)