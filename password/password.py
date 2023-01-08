from cryptography.fernet import Fernet


def Write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def Load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


master_pwd = input("what is your master password?:  ")
key = Load_key() + master_pwd.encode()
fer = Fernet(key)


def view():
    with open('Passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("Uername: ", user, ",", "Password: ",
                  fer.decrypt(passw.encode()).decode())


def add():
    name = input('Account name:  ')
    pwd = input("password:  ")
    with open('Passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input(
        "would you like new or existing one or quit (view / add / q):  "
    ).lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("invalid mode...")
        continue