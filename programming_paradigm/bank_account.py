class BankAccount:
    def __init__(self,initial_balance=0):
        self.account_balance=initial_balance
    def deposit(self,amount):
        if amount>0:
            self.account_balance+= amount            
    
    def withdraw(self, amount):
        if amount > 0 and amount <=self.account_balance:
            if self.account_balance >= amount:
                self.account_balance -= amount

    def display_balance(self):
        print("Current Balance: $"+str((float)(self.account_balance)))

        