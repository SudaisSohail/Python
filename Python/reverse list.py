data = ["a" , "b" , "c" , "d" , "e" , "f" , "g" , "h" , "i"]

# Method 1

for index in range(len(data) // 2):
    data[index] , data[-index - 1] = data[-index - 1] , data[index]

print(data)

# Method 2

data_reversed = []

for number in reversed(data):
    data_reversed.append(number)

print(data_reversed)

# Method 3

data[:] = data[::-1]

print(data)

# Method 4

data.reverse()

print(data)




