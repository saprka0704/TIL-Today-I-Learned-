# using the shuffle(), and sample() to draw winners for the comment event
from random import * # to use the functions of the random module 

user = range(1,21) #class=range
user = list(user)  #change the data structure to 'list'
#print(type(user)) # can check the data structure

shuffle(user) #shuffle the user list

winner = sample(user,4) #draw 4 values of the list

print("-- Winners Announcement --")
print("chicken coupon winner : {}".format(winner[0]))
print("coffee coupon winner : {0}".format(winner[1:]))
print("-- CONGRATULATIONS! --")

