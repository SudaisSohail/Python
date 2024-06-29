# TASK 1

print("Task 1\n")
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")

	
# TASK 2

print("Task 2\n")
n = int(input("Enter a number: "))

for i in range(0, n+1, 2):
    print(i)

# TASK 3

print("Task 3\n")
n = int(input("Enter a number: "))
print(sum(range(1, n+1)))


# TASK 4

print("Task 4\n")
num = int(input("Enter a number: "))

if num == 0 or num == 1:
    print(1)

else:
    answer = 1

    for n in range(2, num+1):
        answer *= n

    print(answer)

# TASK 5

print("Task 5\n")
sum = 0
for i in range(10):
    n = int(input("Enter a number: "))
    sum += n

print(sum / 10)