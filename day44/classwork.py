from decimal import Decimal

class Account():
    
    def __init__(self, name, balance):
        self.name = name
        
        if balance < Decimal(0):
            raise ValueError("Баланс должен быть положительным")
        self.balance = balance
    
    def deposite(self, amount):
        if amount < Decimal(0):
            raise ValueError("Баланс должен быть положительным")
        self.balance += amount
c = Account("VLADIMIR", -2000)

print(c)