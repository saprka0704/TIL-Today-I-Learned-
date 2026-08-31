#Taxi matching program - project
from random import *
    
cnt = 0
for i in range(1,51):
    time = randint(5,50)
    if 5 <= time <= 15: #time in the range (5,16) can be matched
        print("[0] Number {0} passenger (time:{1})".format(i,time))
        cnt += 1  #to count the total number of passengers that were matched
    else: 
        print("[ ] Number {0} passenger (time:{1})".format(i,time)) # match X
print("Number of passengers : {}".format(cnt))