#ch.5

#List
subway = ["Pooh","Piglet", "Tigger"]
print(subway)

print(subway.index("Piglet")) #index function; print the index of the value of the list

subway.append("Eeyore") #append function; add the value to the end of the list
print(subway)

subway.insert(1,"Roo") #insert function; insert the value in the location of the index in the list
print(subway)

print(subway.pop()) #pop function; the last value of the list, deleting it.
print(subway)

subway.clear() #clear function; erase all the value of the list
print(subway)

subway = ["Pooh", "Piglet", "Tigger"]
subway.append("Pooh")
print(subway)
print(subway.count("Pooh")) #count function; count the number of the value in the list

num_list = [5,2,4,3,1]
num_list.sort() #sort function; line up the value in the ascending order
print(num_list)

num_list.sort(reverse=True) # line up the value in the descending order
print(num_list)

num_list.reverse() #reverse function; line up the value in the reverse order
print(num_list)

mix_list = ["Piglet", 5, True]
num_list.extend(mix_list) #extend function; combine two lists together 
print(num_list)

#Dictionary: pair of key and value, one key corresponds with one value -> dictionary name = {key1:value1, key2:value2, ...}
cabinet = {3:"Pooh", 100: "Piglet"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3)) #we can find the value of the corresponding key with the get function
print(cabinet.get(100))

print(cabinet.get(5))
#print(cabinet[5]) #without the key '5' the program malfunctions and shuts down


