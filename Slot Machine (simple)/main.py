
import random
import time

BALANCE = 1000
MIN_BET = 10
MAX_BET = 1000
ICONS = {
    '🍗': 1.5,
    '🍉': 2,
    '🍒': 2.5,
    '🍓': 3,
    '🍀': 4, 
    '🍌': 5
}


def getBet():
    while True:
        amount = input(f"Enter how much you want to bet(${MIN_BET} - ${BALANCE if BALANCE <= MAX_BET else MAX_BET})(q to quit): $")
        if amount.isdigit():
            amount = int(amount)
            if amount <= BALANCE:
                if MIN_BET <= amount <= MAX_BET:
                    return amount
                else:
                    print(f"Amount must be between ${MIN_BET} to ${MAX_BET}")
                    continue
            else:
                print(f"You are exceeding your balance of ${BALANCE}")
                continue
        else:
            if amount == 'q':
                quit()
            print("Must be a number")
            continue

def showVal():
    items = list(ICONS.items())
    for key, value in items:
        print(f"{key} : {value}x")
    print(f"Your current balance: ${BALANCE}")

def roll(amount):
    winnings = 0
    for _ in range(3):
        row = ""
        for _ in range(3):
            icon = random.choice(list(ICONS.keys()))
            row += icon
        for symbol in row:
            print(symbol, end="    ")
            time.sleep(0.5)
        print()
        if row[0] == row[1] == row[2]:
            multiplier = ICONS.get(row[0])
            winnings += amount * multiplier
    return winnings

def ask():
    while True:
        choice = input("Would you like to continue? (y/n): ")
        if choice == 'y':
            break
        elif choice == 'n':
            quit()
        else:
            print("Enter y or n")
            continue

showVal()
while True:
    bet = getBet()
    BALANCE -= bet
    winnings = roll(bet)
    BALANCE += winnings
    print(f"You won ${winnings}")
    print(f"Your current balance: ${BALANCE}")
    if BALANCE < MIN_BET:
        print("You are out of money, minimum betting value is", MIN_BET)
        break
    ask()
    # print(f"Your current balance: ${BALANCE}")
