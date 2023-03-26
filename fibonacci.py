# Task: Enter a number and have the program generate the Fibonacci sequence to that number or to the
# Nth number.

def fibon_seq(number):
    a = 0
    b = 1
    for n in range(number):
        yield a
        a, b = b, a + b

my_seq = fibon_seq(10)
print(my_seq)
print(list(my_seq))
