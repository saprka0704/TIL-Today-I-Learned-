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

print(cabinet.get(5,"available")) #without the key '5' we can use the get function to return the default value, in this case it is 'available'

print(3 in cabinet)
print(100 in cabinet) #use the 'in' operator to check if the exact key is in the dictionary

cabinet = {"A-3": "Pooh", "B-100": "Piglet"}
print(cabinet["A-3"])
print(cabinet["B-100"])

cabinet["A-3"] = "Tigger" #change the value of the key 'A-3'
cabinet["C-20"] = "Eeyore" #add a new key with a new value to the dictionary
print(cabinet)

del cabinet["A-3"] #delete the value of the key
print(cabinet)

print(cabinet.keys()) #check the keys of the dictionary with the keys function
print(cabinet.values()) #check the values of the dictionary with the values function
print(cabinet.items()) #check the corresponding keys and values of the dictionary with the items function

cabinet.clear() #clear all the keys and the values of the dictionary with the clear function
print(cabinet)

#tuple: can't change/add/delete the value of a tuple -> tuple name = (value1, value2, ...)
coffee = ("espresso", "cappuchino")
print(coffee[0])
print(coffee[1])

(departure, arrival) = ("Gimpo", "Jeju")
print(departure, ">", arrival )
(departure, arrival) = (arrival, departure) # use tuples to change the values of the variable easily
print(departure, ">", arrival)

#set: do not allow repetition, and don't guarantee the sequence of the values
my_set = {1,2,3,3,3}
print(my_set)

java={"Pooh", "Piglet", "Tigger"}
python = set(["Pooh", "Eeyore"]) # can define set with set()

print(java & python) #find the intersection of the two set with '&' or intersection function
print(java.intersection(python))

print(java|python) #find the union of the two set with '|' or union function
print(java.union(python))

print(java-python) #find the difference of the two sets with '-' or difference function
print(java.difference(python))

python.add("Piglet") #add a value to the set with the add function
print(python)
java.remove("Piglet") #remove a value of the set with the remove function
print(java)

#change the data structure between list, set and tuples; list = [], tuple = (), set = {}
menu = {"coffee", "milk", "juice"}
menu = list(menu)
print(menu)
print(type(menu))
