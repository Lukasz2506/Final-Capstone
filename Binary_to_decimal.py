# Binary to Decimal and Back Converter - Develop a converter to convert
# a decimal number to binary or a binary number to its decimal equivalent.

def binary_to_decimal(binary):
    # convert binary number to decimal
    power = 0
    result = 0
    binary_list = list(str(binary))
    number = len(binary_list) - 1
    for n in range(len(binary_list)):
        binary_list[n] = int(binary_list[n])
    for n in range(len(binary_list)):
        num_to_check = binary_list[number]
        if num_to_check == 1:
            result += 2**power
            power += 1
            number -= 1
        else:
            power += 1
            number -= 1
    return result


# print(binary_to_decimal(1001001))


def decimal_to_binary(decimal):
    # convert decimal to binary
    binary_list = []
    for n in range(decimal//2):
        number = decimal % 2
        binary_list.insert(0, number)
        decimal = decimal // 2
    while binary_list[0] == 0:
        binary_list.pop(0)
    for n in range(len(binary_list)):
        binary_list[n] = str(binary_list[n])
    return ''.join(binary_list)

# print(decimal_to_binary(11))

program_on = True
print('NUMBERS CONVERTER')
while program_on:
    choice = input('What type of number you want to convert (binary / decimal)').lower().strip()
    if choice == 'binary':
        number = input('type your number')
        converted_number = binary_to_decimal(number)
        print(f'Your binary number {number} is equal to decimal {converted_number}.')
    elif choice == 'decimal':
        number = int(input('type your number'))
        converted_number = decimal_to_binary(number)
        print(f'Your decimal number {number} is equal to binary {converted_number}.')
    else:
        print('No choice found. Try again.')
        continue
    still_continue = input('Do you want to do something else (y / n)?').lower().strip()
    if still_continue == 'y':
        pass
    else:
        print('Good bye!')
        program_on = False




