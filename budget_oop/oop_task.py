class Budget:
    def __init__(self, amount=0):
        self.amount = amount

    def deposit(self, amount):
        self.amount += amount

    def withdraw(self, amount):
        self.amount -= amount

    def transfer(self, other, amount):
        self.withdraw(amount)
        other.deposit(amount)

    def get_balance(self):
        return self.amount




## Use cases

food = Budget(10000)
clothing = Budget(10000)
entertainment = Budget(10000)

food.deposit(3500)
print("Result after depositing in food: {}".format(food.get_balance()))

clothing.withdraw(1700)
print("Result after withdrawing clothing budget: {}".format(clothing.get_balance()))

food.transfer(entertainment, 1000)
print("Result after transferring from food: {} to entertainment budget: {}".format(food.get_balance(), entertainment.get_balance()))
