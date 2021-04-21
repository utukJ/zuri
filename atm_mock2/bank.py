import json
import random


## load database from json if avaaible, else create empty database
try:
    with open("database.txt", mode="r") as f:
        database = json.load(f)
except FileNotFoundError:
    database = {}

# print("database: ", database)


def init():
    print("\n\n")
    print("*"*40)
    print("**********BANK PHP HOME PAGE***********")
    print("*"*40)
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
        return
    password = input("Enter your password: \n")

    if account_number not in database:
        print("Invalid account number!")
        login()
        return
    elif database[account_number][2] != password:
        print("Incorrect password!")
        login()
        return

    print("\n***************LOGIN SUCCESSFUL*****************")
    user_details = database[account_number]
    print(f"Welcome {user_details[0]} {user_details[1]}!")
    bank_operation(account_number)
    logout()
    


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
    selected_option = input("What would you like to do. (1)deposit (2)withdrawal (3)transfer funds (4)check balance (5)Logout \n")

    if selected_option == "1":
        amount = eval(input("How much would you like to deposit: \n"))
        print(deposit(account_number, amount))
    elif selected_option == "2":
        amount = eval(input("How much would you like to withdraw: \n"))
        print(withdrawal(account_number, amount))
    elif selected_option == "3":
        amount = eval(input("How much would you like to transfer: \n"))
        destination = input("Input the account number for the destination: \n")
        print(transfer_funds(account_number, destination, amount))
    elif selected_option == "4":
        check_balance(account_number)
    elif selected_option == "5":
        logout()
        return
    else:
        print("Invalid option selected")
        bank_operation(account_number)

    user_input = input("Want to perform another transaction? yes(1) no(type anything else):\n")
    if user_input == "1":
        bank_operation(account_number)



def can_withdraw(account_number, amount):
    balance = database[account_number][4]
    if balance >= amount:
        return True
    else:
        return False


def withdrawal(account_number, amount):
    if can_withdraw(account_number, amount):
        database[account_number][4] -= amount
        return "Funds withdrawal successful. Take your cash!"
    else:
        return "Insufficient Funds!"


def deposit(account_number, amount):
    database[account_number][4] += amount
    return "Funds deposit successful!\n"


def transfer_funds(source_account_number, target_account_number, amount):
    if can_withdraw(source_account_number, amount):
        withdrawal(source_account_number, amount)
        deposit(target_account_number, amount)
        return "Funds transfer successful!\n"
    else:
        return "Insufficient Funds!"

def check_balance(user_account_number):
    print("Your account balance is {}".format(database[user_account_number][4]))


def generate_account_number():
    return random.randrange(1111111111,9999999999)


def logout():
    with open("database.txt", mode="w") as f:
        json.dump(database, f)
    init()

#### ACTUAL BANKING SYSTEM #####

init()

