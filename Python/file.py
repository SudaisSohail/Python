with open("eg.txt", "wt") as file:
    
    print(file.name)   # Returns the name of the file
    print(file.mode)   # Returns the mode of the file
    
    file.write("Ibrahim is one and a half years old.\n")
    file.write("Sarah is almost six years old.")

with open("eg.txt", "rt") as file:
    
    # All these three read methods continue from where the previous had stopped. 

    data = file.read(10)   # Reads the whole file in the memory, if number of char is passed, it reads only that number of chars
    print(data)
    print(file.tell())     # Returns on which character we are on in the file

    data = file.readline()  # Reads the file line by line as we call it. It generates lines
    print(data)
    print(file.tell())
    
    data = file.readlines()  # Reads the file and make a list of each line in the file
    print(data)

with open("eg.txt", "rt") as file:

    print(file.readable())   # Returns True if the object supports reading from it
    data = file.read(15)
    print(data)

    file.seek(0)          # Sets the cursor of the file to character number given
    print(data)

with open("eg.txt", "wt") as file:

    print(file.writable())   # Returns True if the object supports writing to it

    file.write("Hello World ")
    file.write("Hello Python")

    file.seek(3)

    file.write(" PYTHON ")

    file.seek(0)
    file.write("h")

with open("plane.jpg", "rb") as file:
    with open("plane_copy.jpg", "wb") as pic:
        pic.write(file.read())









