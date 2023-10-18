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
        if self.balance < amount:
            raise Exception
        
        self.balance -= amount


        return self


personsAcc = Account("Nathan ", "Flame ", "de Satan:", 200000)
count = 0;

def pokupka():  
    global personsAcc, count;
    try:

        personsAcc.substractBalance(100000);
        count+=1;
        print('спасибо за покупку айфона', count, personsAcc.balance);
    except:
        print('ошибка транзакции');


pokupka();
pokupka();
pokupka();

print('приходите еще');
