#ch.8;standard input/output
#standard input : input() -> uses keyboard to enter users input
answer = input("What do you want to enter?")
print("Your answer is : "+ answer)
print(type(answer))  # the type of the input is string

#standard output: print()
#separator: the default value of the separator is sep = " "(space) -> separate values by space
print("Python"+"Java")  #PythonJava
print("Python", "Java") #Python Java
print("Python", "Java", sep=",") #Python,Java ; change the separator to "," -> separate the values by comma
print("Python","Java","Javascript", sep=" vs ")   #Python vs Java vs Javascript

#end: the devault value of end is end = "\n" -> changes lines
print("Python", "Java", sep=",")
print("What is more exciting?")  # prints in two lines

print("Python", "Java", sep =",", end=". ") # changed the end to ". "(period) -> One line with a period between.
print("Which is more exciting?") # Python, Java. Which is more exciting?

'''
file : to decide the output destination of the print function
sys.stdout: standard output -> print functions's default output destination(terminal)
sys.stderr: to print an error message when there is a malfunction in the program
log : to record information abouot time, work, the result of the work etc. 
'''
import sys
print("Python", "Java", file=sys.stdout)
print("Python", "Java", file=sys.stderr)


#ljust/rjust
#ljust(): left-jsutified, rjust(): right-justified -> only works with strings
scores = {"Math":0, "English":50, "Coding":100}  #dictionary
for subject, score in scores.items(): #(key,value) pair of the dictionary
    print(subject, score)
'''
Math 0
English 50
coding 100
'''
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":") #left-justified the subjec, right-justified the score
'''
Math    :   0
English :  50
Coding  : 100
'''

#zfill(): fill the blank with 0 to the left of the number to make it a certain length
for num in range(1,21):
    print("Waiting number : " + str(num).zfill(3)) #add 0 to the left of the number to make it 3 digits length -> 001 002 003 ... 020

#format()
print("{0}".format(500))        #500
print("{0:>10}".format(500))    #       500  -> '>'; right-justified / '10': length  /  

print("{0:>+10}".format(500))   #      +500
print("{0:>+10}".format(-500))  #      -500  (to insert the sign of the negative number)

print("{0:_<+10}".format(500))  #+500______

print("{0:,}".format(100000000000)) #100,000,000,000
print("{0:^<+30,}".format(100000000000)) #+100,000,000,000^^^^^^^^^^^^^^

print("{0}".format(5/3))      #1.666666666666667
print("{0:f}".format(5/3))    #1.666667 -> default 6 decimal places
print("{0:.2f}".format(5/3))  #1.67     -> 2 decimal places

#file input/output
score_file=open("score.txt", "w", encoding = "utf8")  #open("file name", "mode", encoding = encoding format) ->"w" mode : write mode, make a new file or cover an existing file with new contents/ encoding -> the character of the content of the file, 'utf8' supports Korean characters.
print("Math: 0", file = score_file)
print("English: 50", file = score_file)
score_file.close()   #you have to close the file after making/writing/editing a file

score_file = open("score.txt", "a", encoding = "utf8") # append mode: to add new content without overwriting the existing content of the file
score_file.write("Scienc: 80\n")
score_file.write("Coding: 100\n") # unlike print function, write function doesn't change lines, to change line we must inclue "\n"
score_file.close()

score_file = open("score.txt", "r", encoding = "utf8") # read mode: to read the content of the existing file
print(score_file.read())  #read function : read the whole content of the file -> printing the content on the terminal
score_file.close()

score_file = open("score.txt", "r", encoding ="utf8")
print(score_file.readline(), end="")  # readline function: reads one line of the file at a time, if we don't include end="", it will add an extra new line
print(score_file.readline(), end="")  # changing lines can be overlappend -> including  end = "" prevents it from happening
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()

#if we don't know how many lines are in the file, we can use a while loop to read the lines until there are no line left to read
score_file = open("score.txt", "r", encoding ="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()

#we can also use readlines function to read all the lines of the file and store them in a list
score_file = open("score.txt", "r", encoding ="utf8")
lines = score_file.readlines()
for line in lines:
    print(line, end="")
score_file.close()

#Pickle
#Pickle is a module that allows us to serialize and deserialize Python objects, which means we can save complex data structures like list and dictionaries to a file and load them back later.
import pickle
profile_file = open("Profile.pickle", "wb") #to save the file using pickle model, the file as to be in a binary form -> write mode: "wb"
profile = {"Name": "Snoopy", "Age": 7, "Hobby": ["Drawing", "Playing", "Reading"]} #dictionary data structure
print(profile)

pickle.dump(profile, profile_file)  #dump funtion: dump(saving data, file name) -> to save the data on the file with pickle module
profile_file.close()

profile_file = open("Profile.pickle", "rb") #open the file in read binary mode("rb")
profile = pickle.load(profile_file) # load function : load(file name) -> to load(recall) data from the file

print(profile)
profile_file.close()

#with statement : automatically closes the file after the block of code is executed, even if an error occurs
with open("Profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

with open("study.txt", "w", encoding = "utf8") as study_file:
    study_file.write("I am studying python hard")

with open("study.txt","r", encoding = "utf8") as study_file:
    print(study_file.read())