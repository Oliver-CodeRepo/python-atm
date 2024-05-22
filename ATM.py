class ATM:
    def __init__(self,balance=0,pin=0000):
        self.balance=balance

        self.pin=pin

    def check_balance(self):
        return self.balance

    def withdraw(self,amount):
        if amount > self.balance:
            return "Insufficient funds."
        else:
            return f"withdrawal successful.Current balance:{self.balance}"

    def deposit(self,amount):
        self.balance += amount
        return f"Your current balance is: {self.balance}"

    def change_pin(self,new_pin):
        self.pin = new_pin
        return"PIN changed successfully"

def main():



