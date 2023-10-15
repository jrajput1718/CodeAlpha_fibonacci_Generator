def  fibonacci(n):

	if n == 1  or n == 0:

		return n

	else:

		return fibonacci(n-2) + fibonacci(n - 1)


number = int(input("Enter the number: "))

if number < 0:
	print("Number not valid")

i = 0

print("fibonacci: ")

for i in range(0, number):
	print(fibonacci(i))