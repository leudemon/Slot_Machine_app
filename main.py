import random
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A" : 3,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        current_symbol = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)
        
        columns.append(column)
    return columns
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=' | ')
            else:
                print(column[row], end="")
        print()
    
            
    
def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else: 
                print("invalid amount.")
        else:
            print("Please enter a valid amount.")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Number of lines to bet on (1-" + str(MAX_LINES)+")? ")
        if lines.isdigit():
            lines = int(lines)
            if MAX_LINES >= lines >= 1:
                break
            else: 
                print("invalid numnber of lines.")
        else:
            print("Please enter a valid number of lines.")
    return lines

def get_bet():
    while True:
        amount = input("How much would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MAX_BET >= amount >= MIN_BET:
                break
            else: 
                print("invalid amount.")
        else:
            print("Please enter a valid amount.")
    return amount

def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = lines * bet
        if  (total_bet > balance):
            print("Not enough funds. current balance: ${}".format(balance))
            break
        else:
            print("You are betting ${2} on {1} line(s). total bet ${0}".format(total_bet, lines, bet))
            balance = balance - total_bet
            print("Balance: {}".format(balance))
            slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
            print_slot_machine(slots)
            
    
    
    #print(balance, lines, bet)
    
    
main()