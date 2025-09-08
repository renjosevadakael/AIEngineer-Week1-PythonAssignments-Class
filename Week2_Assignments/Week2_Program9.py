""" Assignment Details: 
 
Create a Python class named BankAccount to represent and manage basic banking operations. 
 
Requirements: 
a) Create a class named BankAccount. 
b) Inside the class, define the following attributes: 
1. account_holder → string 
2. balance → float 
3. account_type → string (e.g., "Savings" or "Current") 
c) Implement the following methods: 
1. deposit(amount) → increases the balance by the given amount. 
2. withdraw(amount) → decreases the balance by the given amount if sufficient funds are 
available, otherwise display "Insufficient balance". 
3. display_balance() → prints the account holder’s name, account type, and current 
balance. 
d) In the main section (if __name__ == "__main__":): 
 Create at least two BankAccount objects with different details. 
 Perform deposit and withdrawal operations. 
 Display the account details after each operation. """

class BankAccount:
    def __init__(self,account_holder:str,balance:float,account_type:str):
        self.account_holder=account_holder
        self.balance=balance
        self.account_type=account_type
    def deposit(self,amount:float):
        self.balance+=amount
    def withdraw(self,amount):
        if(self.balance>=amount):
            self.balance-=amount
        else:
            print("Insufficient balance")
    def display_balance(self):
        print(f"Account holder’s name {self.account_holder} , account type {self.account_type}, and current balance {self.balance}")
    
    
if __name__ == "__main__":
    bankAccount1 = BankAccount("Renju",12000.56,"Savings")
    bankAccount2 = BankAccount("Rajesh",12000000.96,"Current")

#Perform Deposit
print("Balance before Deposit")
bankAccount1.display_balance()
bankAccount1.deposit(2000.09)
print("Balance after Deposit")
bankAccount1.display_balance()

#Perform Withdrawal
print("Balance before Withdrawal")
bankAccount2.display_balance()
bankAccount2.withdraw(29800.09)
print("Balance after Withdrawal")
bankAccount2.display_balance()
