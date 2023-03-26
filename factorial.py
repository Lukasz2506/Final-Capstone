# Factorial Finder - The Factorial of a positive integer, n, is defined as the product of the sequence n,
# n-1, n-2, ...1 and the factorial of zero, 0, is defined as being 1. Solve this using both loops and
# recursion.

def factorial(number):
    result = 1
    for n in range(1, number + 1):
        result = result * n
    return result


print(factorial(0))
print(factorial(4))