#Calculate the standard weight using the formula based on height and gender

def std_weight(height, gender): #define a function named std_weight with parameters height and gender
    if gender == "male":
        return height*height*22 
    else:
        return height*height*21

height =175
gender = "male"
weight = round(std_weight(height/100, gender), 2) #rounding to 2 decimal places
print("The Standard weight for a {0}cm tall {1} is {2}kg.".format(height, gender, weight)) #The Standard weight for a 175cm tall male is 67.38kg.

height =160
gender = "female"
weight = round(std_weight(height/100, gender), 2) 
print("The Standard weight for a {0}cm tall {1} is {2}kg.".format(height, gender, weight)) #The Standard weight for a 160cm tall female is 53.76kg.