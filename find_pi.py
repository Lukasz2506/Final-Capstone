# Task: Enter a number and have the program generate PI up to that many decimal places. Keep a limit to how far the program will go.

import math

pi = math.pi
program = True
while program == True:
    how_many_dec = int(input('How many decimal places you\'d like to display (max 10)? '))
    if how_many_dec <= 10:
        print(f'{pi:.{how_many_dec}f}')
    elif how_many_dec > 10:
        print('Max 10 decimal places. try Again')
    elif how_many_dec < 0:
        print('Decimal places cannot be less than zero. Try again.')
    still_try = input('Would you like to try again (y / n)?').lower().strip()
    if still_try == 'y':
        pass
    else:
        program = False