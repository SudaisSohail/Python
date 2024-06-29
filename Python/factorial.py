def factorial(num):

	if num == 0 or num == 1:

		return 1

	elif num < 0:

		answer = -1

		for n in range(2, -(num) + 1):

			answer *= n

		return answer

	elif num > 0:

		answer = 1

		for n in range(2, num + 1):

			answer *= n

		return answer

print(factorial(0))
