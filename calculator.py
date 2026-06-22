x= float(input("what's x?"))
y= float(input("what's y?"))
#int: integer, float: decimal number, str: string of characters
#z= round(x + y)

#round(number[, ndigits])
#z= round(x / y, 2)

z= x / y

#the way you specify the number of decimal places is by using the f string
print(f"{z:.2f}")

#automatically adds commas to the number -> format specifier
#print(f"{z:,}")

def main():
    x= int(input("what's x?"))
    print("x squared is", square(x))

def square(n):
    return n * n
#return: the value that is returned from the function; the output of the function
main()