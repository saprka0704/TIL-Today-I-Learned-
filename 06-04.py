#making calculators with python coding
x = float(input("what is x?"))  
y = float(input("what is y?"))
#int: interger, float: decimal number, string: text 

#print(x+y) -> it print's out as a sum of x and y as a number 
#z=round(x+y) -> it will round it to the nearest integer
#z=round(x/y,2) #rounds to 2 decimal places

#round(number[,ndigits]): round the number on the nth digit, if ndigits is not given, it rounds to the nearest integer.

z = x/y
print(f"{z:.2f}")
