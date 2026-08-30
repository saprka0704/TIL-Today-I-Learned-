#ch6. statements
#if statement : conditional statements
weather = "Raining"
if weather == "Raining":
    print("Bring your umbrella")
elif weather == "Dusty":  #when you want to add multiple conditions
    print("Wear a mask outdoors")
else : 
    print("No supplies needed!")  #if the conditions don't match 

temp = int(input("What's the temperature today?")) #to ask and enter a value
if 30 <= temp:
    print("Too hot. Avoid going outdoors!")
elif 10<= temp <= 30:
    print("Moderate for outdoor activities!!")
elif 0<= temp <= 10:
    print("Take your coat with you")
else: 
    print("Freezing! Avoid going outside!")

# loop : to repeat an action
# for loop
orders = ["Ironman","Thor","Spiderman"]
for customer in orders:
    print("{}, your coffe is ready!".format(customer))

#while loop : repeat the action while the condition is approved
customer = "Thor"
index = 5
while index >= 1:
    print("{}, your coffe is ready!".format(customer))
    index -=1
    print("{} times left!".format(index))
    if index == 0:
        print("Discarding the coffee~!")
       

#continue & break: continue to the next repeating target/ to break the loop and escape
absent = [2,5]
no_book = [7]

for student in range(1,11):
    if student in absent:
        continue
    elif student in no_book:
        print("That's all for today's class. Number {} student, please follow me to the teacher's office!".format(no_book))
        break
    print("Number {0} student, read the book aloud please!".format(student))

students = ["Ironman", "Thor", "Spiderman"]
students = [len(i) for i in students]
print(students)