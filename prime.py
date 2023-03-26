# Task Enter a number and have the program generate the Fibonacci sequence to that number or to the
# Nth number.

number = int(input('type a number: '))

not_prime = []
for i in range(2, number + 1):
    if i > 1:
        if number % i == 0:
            not_prime.append(i)
if len(not_prime) > 1:
    print(f'{number} is not a prime number')
else:
    print(f'{number} is a prime number')

