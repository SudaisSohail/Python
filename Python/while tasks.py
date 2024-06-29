# TASK 1

n = 10
sum = 0

while n != 0:
    num = int(input("Enter a number: "))
    sum += num
    n -= 1

print(sum)

# TASK 2

num = int(input("Enter a number: "))
sum = 0

while num != 0:
    sum += num
    num -= 1

print(sum)

# TASK 3

num = int(input("Enter a number: "))
counter = 1
sum = num

while num != 0:
    num = int(input("Enter a number: "))
    sum += num
    counter += 1

print(f"Average: {sum / counter}")