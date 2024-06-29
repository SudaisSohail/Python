with open("eg.txt", "r") as file:

    memo = file.read()
    print(file.closed)
    print(memo)

print(file.closed)

