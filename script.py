"""
This script has basic coding which is >=30 lines in Python3. 
"""
print("Hello, World!")
print("This is a sample code for STT LAB 1")

print("Print the first 10 numbers")
for i in range(10):
    print(i)
if i < 10:
    print("i is less than 10")
else:
    print("i is greater than 10")

def func(n):
    """
    This is a sample function that print factors of a number n given as argument to the function.
    """
    print("This is a function")
    print(f"The factors of the number {n} are:")
    for f in range(1, n+1):
        if(n % f == 0):
            print(f)
func(i)

print("Squares of the first 5 numbers:")
for j in range(5):
    print(f"Square of {j} is {j**2}")

def factorial(x):
    """
    This factorial function finds the factorial of given number. 
    """
    fact = 1
    for i in range(1, x + 1):
        fact *= i
    return fact

print("Factorial of numbers from 1 to 5:")
for m in range(1, 6):
    print(f"Factorial of {m} is {factorial(m)}")
