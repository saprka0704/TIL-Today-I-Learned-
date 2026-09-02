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

# calling out the function
def profile(name, age, main_lang):
    print("Name:{0}\t Age:{1}\t Main Language:{2}".format(name, age, main_lang))

profile("Charlie", 20, "Python")
profile("Lucy", 25, "Java")

def profile(name, age=20, main_lang = "Python"): #default value
    print("Name:{0}\t Age:{1}\t Main Language:{2}".format(name, age, main_lang))

profile("Charlie") #Name : Charlie   Age : 20        Main language : Python
profile("Lucy") #Name : Lucy   Age : 20        Main language : Python

profile("Charlie",22) #Name : Charlie   Age : 22        Main language : Python
profile("Lucy",24,"Java")  #Name : Lucy   Age : 24        Main language : Java

#keyword argument
def profile(name, age, main_lang):
    print(name, age, main_lang) 

profile(name="Charlie", main_lang="Python", age=20) #Charlie 20 Python
profile(main_lang="Java", age=25, name="Lucy") #Lucy 25 Java

def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("Name:{0}\t Age:{1}\t".format(name, age), end=" ") #end=" " : to avoid line break -> changes the line(enter key)
    print(lang1, lang2, lang3, lang4, lang5)

profile("Charlie", 20, "Python", "Java", "C", "C++", "C#") #Name: Charlie   Age: 20        Python Java C C++ C#
profile("Lucy", 25, "Kotlin", "Swift", "", "", "") #if there is no value, just leave it blank -> Name: Lucy   Age: 25        Kotlin Swift

#variable argument: argument that can take multiple values
def profile(name, age, *language): #*language : variable argument -> recognizes multiple values as a tuple
    print("Name:{0}\t Age:{1}\t".format(name, age), end=" ")
    print(language, type(language))

profile("Charlie", 20, "Python", "Java", "C", "C++", "C#", "Javascript") #Name: Charlie   Age: 20        ('Python', 'Java', 'C', 'C++', 'C#', 'Javascript') <class 'tuple'>
profile("Lucy", 25, "Kotlin", "Swift") #Name: Lucy   Age: 25        ('Kotlin', 'Swift') <class 'tuple'>

def profile(name, age, *language):
    print("Name:{0}\t Age:{1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ") #end=" " : to avoid line break -> changes the line(enter key)
    print() #to add a line break

profile("Charle", 20, "Python", "Java", "C", "C++", "C#", "Javascript") #Name: Charlie   Age: 20        Python Java C C++ C# Javascript
profile("Lucy", 25, "Kotlin", "Swift") #Name: Lucy   Age: 25        Kotlin Swift

#local variable and global variable
glasses = 10 #globla variable -> varible that can be used anywhere in the code
def rent(people):
    #glasses = 20 -> local variable that can only be used inside the function
    global glasses #to use the global variable inside the function
    glasses -= people
    print("[Inside the function] Remaining 3D glasses: {0}".format(glasses))

print("Total 3D glasses: {0}".format(glasses)) # Total 3D glasses: 10
rent(2) #people = 2 -> [Inside the function] Remaining 3D glasses: 8
print("Remaining 3D glasses: {0}".format(glasses)) # Remaining 3D glasses: 8

#without using the global variable, we can use the return value to update the global variable
glasses = 10
def rent_return(glasses, people):
    glasses -= people
    print("[Inside the function] Remaining 3D glasses: {0}".format(glasses))
    return glasses

print("Total 3D glasses: {0}".format(glasses)) # Total 3D glasses: 10
glasses = rent_return(glasses, 2) #people = 2 -> [Inside the function] Remaining 3D glasses: 8
print("Remaining 3D glasses: {0}".format(glasses)) # Remaining 3D glasses: 8