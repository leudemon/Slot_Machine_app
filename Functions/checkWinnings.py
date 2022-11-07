from Functions import checkWinnings
from Functions import get_bet
from Functions import get_deposit
from Functions import number_of_lines
from Functions import slot_machine_output
from Functions import slot_machine_spin
from Functions import spin
from Functions import config

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
