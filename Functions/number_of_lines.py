from Functions import checkWinnings
from Functions import get_bet
from Functions import get_deposit
from Functions import number_of_lines
from Functions import slot_machine_output
from Functions import slot_machine_spin
from Functions import spin
from Functions import config


def get_number_of_lines():
    while True:
        lines = input("Number of lines to bet on (1-" +
                      str(config.MAX_LINES)+")? ")
        if lines.isdigit():
            lines = int(lines)
            if config.MAX_LINES >= lines >= 1:
                break
            else:
                print("invalid numnber of lines.")
        else:
            print("Please enter a valid number of lines.")
    return lines
