import math

def change(money):
    coin_dict = {'quarter': 0.25, 'dime': 0.1, 'nickel': 0.05, 'penny': 0.01}
    change = {}
    money_sum = money
    for coin in coin_dict:
        if coin_dict[coin] <= money_sum:
            division = money_sum / coin_dict[coin]
            no_of_coins = math.floor(division)
            change[coin] = no_of_coins
            money_sum -= no_of_coins*coin_dict[coin]
        else:
            pass
    print('Here is your change')
    for coin, number in change.items():
        print(f'{coin}: {number}')

change(2.56)