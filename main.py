import random
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 3,
    "B": 4,
    "C": 6,
    "D": 8
}
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


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


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = lines * bet
        if (total_bet > balance):
            print("Not enough funds. current balance: ${}".format(balance))
            exit()
        else:
            break

    print("You are betting ${2} on {1} line(s). total bet ${0}".format(
        total_bet, lines, bet))
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print("You won ${}".format(winnings))
    print(f"You won on lines:", *winning_lines)

    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print("Balance: {}".format(balance))
        answer = input("Press enter to spin(Q) to quit")
        if answer == "q":
            break
        balance += spin(balance)


main()
