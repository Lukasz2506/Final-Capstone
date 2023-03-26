# Task description: Change Return Program - The user enters a cost and then the amount of money
# given. The program will figure out the change and the number of quarters, dimes, nickels, pennies
# needed for the change.
import math

goods = {'snickers': 2.5, 'waffer': 1.25, 'juice': 3.5, 'chips': 2.25}

def change(money):
    coin_dict = {'quarter': 0.25, 'dime': 0.1, 'nickel': 0.05, 'penny': 0.01}
    change = {}
    money_sum = money
    for coin in coin_dict:
        if coin_dict[coin] <= money_sum:
            division = money_sum / coin_dict[coin]
            no_of_coins = math.floor(division)
            change[coin] = no_of_coins
            money_sum -=  no_of_coins*coin_dict[coin]
        else:
            pass
    print('Here is your change')
    for coin, number in change.items():
        print(f'{coin}: {number}')



print('The snack vending machine')
buying_process = True
while buying_process:
    what_snack = input('Choose the snack you would like to buy (snickers, waffer, juice, chips)').lower().strip()
    if what_snack in goods.keys():
        price = goods[what_snack]
        credit = float(input('How much money do you put into machine?'))
        if credit < price:
            print('Not enough money to but this product')
            continue
        elif credit > price:
            print('product withdrawing in progress')
            change(credit-price)
            print('Take you product from the drawer. Enjoy! :)')
            next_product = input('Do you want to buy next product? (y / n)').lower().strip()
            if next_product == 'y':
                continue
            else:
                print('Good bye!')
                buying_process = False
    else:
        what_next = input('This product is not available. Try again (y / n)?').lower().strip()
        if what_next == 'y':
            pass
        else:
            print('Good bye!')
            buying_process = False



