#operators
#augmented assignment operators
number = 5*3+2
number *=4
print(number)

#math module
from math import * #to use every function of the module 'math'
result=floor(4.99)
print(result)
result=ceil(3.14)
print(result)
result=sqrt(16)
print(result)

import math
result=math.floor(4.99)
print(result)
result=math.ceil(3.14)
print(result)
result=math.sqrt(16)
print(result)

#random module
from random import *
print(random()) #randomly chooses any number from 0 to 1(excludes 1)
print(random()*10) #randomly chooses any number from 0 to 10(excludes 10)
print(int(random()*10))

print(randrange(1,46)) #randomly chooses an integer from 1 to 45(excludes 46)
print(randint(1,45)) #randomly chooses an integer from 1 to 45(includes 45)
