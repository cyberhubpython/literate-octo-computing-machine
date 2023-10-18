class Account:
    def __init__(self, name, sirname, fathername, balance):
        self.name = name
        self.sirname = sirname
        self.fathername = fathername
        self.balance = balance
    def infoAccount(self):
        print("This specific account's data is: " + self.name + self.sirname + self.fathername, + self.balance)
    def addBalance(self, amount):
        self.balance += amount
    def substractBalance(self, amount):
        self.balance -= amount

personsAcc = Account("Nathan ", "Flame ", "de Satan:", 200000)