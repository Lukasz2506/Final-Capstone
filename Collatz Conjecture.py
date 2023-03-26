# Collatz Conjecture - Start with a number n > 1. Find the number of steps it takes to reach one
# using the following process: If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.

def collatz_conjecture(number):
    value = number
    number_of_steps = 0
    while value != 1:
        if value % 2 == 0:
            value /= 2
            number_of_steps += 1
        else:
            value *= 3
            value += 1
            number_of_steps += 2
    return number_of_steps


print(collatz_conjecture(1))
print(collatz_conjecture(4))
print(collatz_conjecture(7))
print(collatz_conjecture(3))