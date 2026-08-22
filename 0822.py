#ch.4;strings

#slicing
#index points out the location of a character in a string
birthday="20070418"
print("My birthday is " + birthday[4:]) #uses ':' to mark the starting point and the finishing point

#functions
python="Python is Amazing"
print(python.lower()) #change the strings to lower case
print(python.upper()) #change the strings to upper case
print(python[0].isupper()) #check if the character on index '0' is a lower case
print(python[1:5].islower()) #check if the characters on index 1 to 5 are upper cases
print(python.replace("Python","Java")) #replace the substring "Python" to "Java"

find = python.find("n") #the index of the first occurence of n
print(find)
find = python.find("n", find+1) #the index of the next occurence of n
print(find)
find = python.find("Java") #returns the value -1 if it can't find the substring
print(find)

index = python.index("n")
print(index)
index = python.index("n", index+1) 
print(index)
index = python.index("n", 2, 6)
print(index)
#index = python.index("Java") #If it can't find the substring, malfunction happens and the program shuts down.
#print(index)

print(python.count("n")) #count the number of the character n
print(python.count("v"))
print(len(python)) #find the length of the string


#string formatting-to place a value or a variable in a particular place as a string
#format specifier
print("I am %dyears old." %20) # %d;decimal(integer)
print("My name is %s." % "Sooah") # %s;string
print("The first letter of Apple is %c." %"A") # %c;character
print("My favorite color is %s and %s." %("blue", "purple"))

#format()function
print("I am {}years old".format(20))
print("My name is {}".format("Sooah"))
print("My favorite color is {0} and {1}".format('blue','purple'))
print("My favorite color is {1} and {0}".format('blue','purple'))
print("My name is {name} and I am {age}years old.".format(age=20, name='Sooah'))

#f-string
age=20
name='Sooah'
print(f"My name is {name} and I am {age}years old.")


#escape character
print("He is a ten\nbut...") #\n changes lines
print("He is \"The Spiderman\"!") #\'or \" lets you use (double) quotation mark inside the string 
print("\\Workspace\\TIL-Today-I-Learned-(main)")

print("Red apple\rPine")
print("Redd\bapple")
print("Red\tapple")