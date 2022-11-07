from Functions import checkWinnings
from Functions import get_bet
from Functions import get_deposit
from Functions import number_of_lines
from Functions import slot_machine_output
from Functions import slot_machine_spin
from Functions import spin
from Functions import config

ROWS = config.ROWS
COLS = config.COLS
symbol_count = config.symbol_count


def spin(balance):
    lines = number_of_lines.get_number_of_lines()
    while True:
        bet = get_bet.get_bet()
        total_bet = lines * bet
        if (total_bet > balance):
            print("Not enough funds. current balance: ${}".format(balance))
            exit()
        else:
            break

    print("You are betting ${2} on {1} line(s). total bet ${0}".format(
        total_bet, lines, bet))
    slots = slot_machine_spin.get_slot_machine_spin(ROWS, COLS, symbol_count)
    slot_machine_output.print_slot_machine(slots)
    winnings, winning_lines = checkWinnings.check_winnings(
        slots, lines, bet, config.symbol_value)
    print("You won ${}".format(winnings))
    print(f"You won on lines:", *winning_lines)

    return winnings - total_bet
