class bank:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, money):
        self.money = money
        self.balance = self.balance + self.money
        print('You have',self.balance)
    def withdraw(self, money):
        self.money = money
        if self.money <= self.balance:
            self.balance = self.balance - self.money
            print(self.balance, "left" )

        else:
            print(self.owner, " you cannot fool us")
wallet = bank('Manarbek', 500000)
wallet.withdraw(500)
wallet.deposit(500)