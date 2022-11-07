from Functions import checkWinnings
from Functions import get_bet
from Functions import get_deposit
from Functions import number_of_lines
from Functions import slot_machine_output
from Functions import slot_machine_spin
from Functions import spin
from Functions import config


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=' | ')
            else:
                print(column[row], end="")
        print()
