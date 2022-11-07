import random
from Functions import checkWinnings
from Functions import get_bet
from Functions import get_deposit
from Functions import number_of_lines
from Functions import slot_machine_output
from Functions import slot_machine_spin
from Functions import spin
from Functions import config


def main():
    balance = get_deposit.deposit()
    while True:
        print("Balance: {}".format(balance))
        answer = input("Press enter to spin(Q) to quit")
        if answer == "q":
            break
        balance += spin.spin(balance)


main()
