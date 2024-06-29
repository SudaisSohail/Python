num = int(input("Enter a number: "))
counter = 0
sum = num

while num != 0:
    num = int(input("Enter a number: "))
    sum += num
    counter += 1

print(f"Average: {sum / counter}")