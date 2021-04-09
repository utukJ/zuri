import json
import random



try:
    with open("database.txt", mode="r") as f:
        database = json.load(f)
except FileNotFoundError:
    database = {}

print("database: ", database)

def init():
    print("Welcome to bankPHP")
    user_choice = int(input("Do you want to login or register a new account: login(1) register(2) exit(3)\n"))
    if(user_choice == 1):
        login()
    elif(user_choice == 2):
        register()
    elif(user_choice == 3):
        return
    else:
        print("You have selected invalid option")
        init()


def login():
    print("\n********* Login ***********")

    account_number = input("Input you account number here. Input 7 if you've forgotten \n")
    if account_number == "7":
        print("To retrieve your account number, you need your email and your password!")
        retrieve_acc_number()
        login()
    password = input("Enter your password: \n")

    if account_number not in database:
        print("Invalid account number!")
        login()
    if database[account_number][2] != password:
        print("Incorrect password!")
        login()

    print("\n***************LOGIN SUCCESSFUL*****************")
    user_details = database[account_number]
    print(f"Welcome {user_details[0]} {user_details[1]}!")
    bank_operation(account_number)
    


def register():

    print("\n****** Register *******")

    first_name = input("Input your first name here:  \n")
    last_name = input("Input your last name here: \n")
    email = input("Input your email address here: \n")
    password = input("create a password for yourself \n")
    account_number = generate_account_number()
    balance = 0

    database[str(account_number)] = [first_name, last_name, password, email, balance]

    print("Your Account Has been created")
    print(" == ==== ====== ===== ===")
    print("Your account number is: %d" % account_number)
    print("Make sure you keep it safe")
    print(" == ==== ====== ===== ===")

    login()

def retrieve_acc_number():
    email = input("Enter your email address: \n")
    password = input("Enter your password: \n")
    for acc_number in database:
        if (database[acc_number][3], database[acc_number][2]) == (email, password):
            print("Your account number is {}".format(acc_number))
            return
    print("Your details do not exist!")

def bank_operation(account_number):
    selected_option = input("What would you like to do. (1)deposit (2)withdrawal (3)transfer funds (4)Logout \n")

    if selected_option == "1":
        amount = eval(input("How much would you like to deposit: \n"))
        deposit(account_number, amount)
    elif selected_option == "2":
        amount = eval(input("How much would you like to withdraw: \n"))
        withdrawal(account_number, amount)
    elif selected_option == "3":
        amount = eval(input("How much would you like to transfer: \n"))
        destination = input("Input the account number for the destination: \n")
        transfer_funds(account_number, destination, amount)
    elif selected_option == "4":
        logout()
        return
    else:
        print("Invalid option selected")
        bank_operation(account_number)

    user_input = input("Want to perform another transaction? yes(1) no(type anything else):\n")
    if user_input == "1":
        bank_operation(account_number)


def withdrawal(account_number, amount):
    database[account_number][4] -= amount
    print("Funds withdrawal complete. Take your cash!\n")

def deposit(account_number, amount):
    database[account_number][4] += amount
    print("Funds deposit complete!\n")

def transfer_funds(source_account_number, target_account_number, amount):
    withdrawal(source_account_number, amount)
    deposit(target_account_number, amount)
    print("Funds transfer complete!\n")

def generate_account_number():
    return random.randrange(1111111111,9999999999)

def logout():
    with open("database.txt", mode="w") as f:
        json.dump(database, f)

#### ACTUAL BANKING SYSTEM #####

init()

