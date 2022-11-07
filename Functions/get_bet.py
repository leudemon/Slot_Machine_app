from Functions import config


def get_bet():
    while True:
        amount = input("How much would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if config.MAX_BET >= amount >= config.MIN_BET:
                break
            else:
                print("invalid amount.")
        else:
            print("Please enter a valid amount.")
    return amount
