def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
your_number =int(input("Enter a number:"))
print(f"The factorial of {your_number} is {factorial(your_number)}")