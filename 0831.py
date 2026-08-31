#ch.7:functions
#to define a function
def open_account(): #define a function by using the keyword 'def'
    print("Oppening a new account")

open_account() #call out the function

def deposit(balance, money): #using the parameter to insert values to the function
    print("Depositing {0}$. Remaining balance is {1}$".format(money, balance + money))
    return balance + money #returning value = balance + money

balance=0
balance = deposit(balance, 2000) 

def withdraw(balance, money):
    if balance >= money:
        print("Withdrawing {0}$. Remaining balance is {1}$".format(money, balance - money))
    else:
        print("Withdrawal failure. Remaining balance is {1}$".format(balance))
    return balance - money
    
balance = withdraw(balance, 500)

def withdraw_night(balance, money):
    commission = 100
    print("Withdraw {}$ during non-working hours.".format(money))
    return commission, balance-money-commission

commission, balance = withdraw_night(balance, 700) #form of a tuple
print("Commission fee is {}$, remaining balance is {}$.".format(commission, balance))

