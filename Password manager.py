from cryptography.fernet import Fernet


def write_key():
    k = Fernet.generate_key()
    with open("key.key", 'wb') as f:
        f.write(k)


def load_key():
    with open('key.key', 'rb') as f:
        k = f.read()
    return k


#write_key()
key = load_key()
#print("Your key is: ", key.decode(), "\nkeep the key safe for future use\n")
key = input("Enter key: ").encode()
fer = Fernet(key)


def view():
    with open('password.txt', 'r') as f:
        for line in f:
            line = line.rstrip()
            u, p = line.split('|')
            print("username:", u, " password:", (fer.decrypt(p.encode())).decode())


def add():
    u = input("Enter the username: ")
    p = input("Enter the password: ")
    with open("password.txt", 'a') as f:
        f.write(u + "|" + fer.encrypt(p.encode()).decode() + "\n")


while 1:
    ans = input("Do want to view or add usernames and passwords or exit? (view/add/exit): ").lower()
    if ans == "view":
        view()
    elif ans == "add":
        add()
    elif ans == 'exit':
        exit()
    else:
        print("Invalid choice")
