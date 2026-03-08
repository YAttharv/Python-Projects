import random

words = ("apple", "banana", "coconut", "jackfruit", "mango", "pineapple")

#dictionary of tuple
art = {
    0: ("   ",
        "   ",
        "   "),
    1: (" O ",
        "   ",
        "   "),
    2: (" O ",
        " | ",
        "   "),
    3: (" O ",
        "/| ",
        "   "),
    4: (" O ",
        "/|\\",
        "   "),
    5: (" O ",
        "/|\\",
        "/  "),
    6: (" O ",
        "/|\\",
        "/ \\"),
}

def display_man(wrong_guesses):
    print("*|***")
    for line in art[wrong_guesses]:
        print(line)
    print("*****")

def show_hint(hint:str):
    for letter in hint:
        print(letter + " ", end="")
    print()

def get_letter():
    while True:
        guess = input("Enter an alphabet(0 to quit): ").lower()
        if guess == '0':
            exit()
        if len(guess) != 1:
            print("Enter only one alphabet")
            continue
        if 97 <= ord(guess) <= 122:
            return guess
        else:
            print("Input must be an alphabet (a-z)")

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    while True:
        display_man(wrong_guesses)
        show_hint(hint)
        guess = get_letter()
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = answer[i]
        else:
            wrong_guesses += 1
        string = "".join(hint)
        if string == answer:
            show_hint(hint)
            print("You won")
            break
        if wrong_guesses == 6:
            display_man(wrong_guesses)
            print("You lost")
            print(f"The word was '{answer}'")
            break
        

if __name__ == "__main__":
    main()
