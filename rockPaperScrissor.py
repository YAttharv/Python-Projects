import random

def getUserChoice():
    userChoice = input("Rock, Paper, Scrissor? (r/p/s): ").lower()
    while userChoice not in ['r', 'p', 's']:
        print("Invalid choice!")
        userChoice = input("Rock, Paper, Scrissor? (r/p/s): ").lower()
    return userChoice

def determineWinner(userChoice):
    compChoice = random.choice(['r', 'p', 's'])
    if (compChoice == 'r'):
        if userChoice == 'r':
            result = "tie"
        elif userChoice == 'p':
            result = "user"
        else:
            result = "comp"
    elif (compChoice == 'p'):
        if userChoice == 'r':
            result = "comp"
        elif userChoice == 'p':
            result = "tie"
        else:
            result = "user"
    elif userChoice == 'r':
        result = "user"
    elif userChoice == 'p':
        result = "comp"
    else:
        result = "tie"
    print(compChoice)
    return result

Continue = 'y'
while Continue == 'y':
    userChoice = getUserChoice()
    result = determineWinner(userChoice)
    if result == 'comp':
        print("You Lost!")
    elif result == 'user':
        print("You Won!")
    else:
        print("Tie")
    Continue = input("continue? (y/n): ")