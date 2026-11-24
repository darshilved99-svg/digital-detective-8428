def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


number = int(input("Enter a positive number: "))

if number < 1:
    print("Please enter a number greater than 0.")
else:
    print("Factorial:", factorial(number))