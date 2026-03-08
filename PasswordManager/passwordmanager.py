def encrypt(data: str, key: int): # only aplphabets, numbers and spaces
    encrypt = ""
    for i in data:
        if i.isdigit():
            key_num = key % 10
            append = ord(i) + key_num
        else:
            append = ord(i) + key

        if i == ' ':
            encrypt += ' '
            continue
        elif i == '|':
            encrypt += '|'
            continue
        elif i == '\n':
            encrypt += '\n'
            continue
        elif i.islower():
            if append < ord('a'):
                append += 26
            elif append > ord('z'):
                append -= 26
        elif i.isupper():
            if append < ord('A'):
                append += 26
            elif append > ord('Z'):
                append -= 26
        elif i.isdigit():
            if append < ord('0'):
                append += 10
            elif append > ord('9'):
                append -= 10
        encrypt = encrypt + chr(append)
    return encrypt

def decrypt(data: str, key: int):
    key = 0 - key
    return encrypt(data, key)


def view(key: int):
    with open("D:\My\Coding\Code\Python Projects\PasswordManager\passwords.txt", 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            data = decrypt(data, key)
            user, pwd = data.split("|")
            print("User: " + user + "\n" + "Password: " + pwd + '\n')

def add(key: int):
    acc = input("Account name: ")
    pwd = input("Password: ")
    with open("D:\My\Coding\Code\Python Projects\PasswordManager\passwords.txt", 'a') as f:
        f.write(encrypt(acc + "|" + pwd + "\n", key))

while True:
    mode = input("View existing password or add new one (view / add)(q to quit): ").lower()
    if mode == 'q':
        break
    while True:
        key = input("Enter key: ")    
        if key.isdigit():
            key = abs(int(key))
            break
        print("key should be a number")
    key %= 26

    if mode == "view":
        view(key)
    elif mode == "add":
        add(key)
    else:
        print("Invalid input")
