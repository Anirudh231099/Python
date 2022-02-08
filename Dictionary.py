#Accessing an element
# mydictionary = { 1: 'Rohit' , 2: 'Dhawan' , 3: 'Virat'}
# print(mydictionary[1])
# print(mydictionary.get(2))
# print(len(mydictionary))

#Replacing an element
# mydictionary = { 1: 'Rohit Sharma' , 2: 'Shikhar Dhawan' , 3: 'Virat Kohli'}
# mydictionary[3] = 'Rishab Pant'
# print(mydictionary)

#Removing an element
# mydictionary = { 1: 'Rohit' , 2: 'Dhawan' , 3: 'Virat'}
# del mydictionary[3]
# print(mydictionary)

# #clear( ) – removes all the elements from the dictionary.
# a = { 1: 'Rohit' , 2: 'Dhawan' , 3: 'Virat'}
# a.clear()
# print(a)

#copy( ) – returns a copy of the dictionary.
# a = { 1: 'Rohit' , 2: 'Dhawan' , 3: 'Virat'}
# b = a.copy()
# print(b)

#values( ) – returns all the values in a dictionary.
# a = { 1: 'Rohit' , 2: 'Dhawan' , 3: 'Virat'}
# print(a.values())

#keys( ) – returns a list containing all the keys in the dictionary.
# a = { 1: 'Rohit' , 2: 'Dhawan' , 3: 'Virat'}
# print(a.keys())

#items( ) – returns a tuple of each key value pair in the dictionary.
# a = { 1: 'Rohit' , 2: 'Dhawan' , 3: 'Virat'}
# print(a.items())

#pop( ) – removes the element with the specified key.
# a = { 1: 'Rohit' , 2: 'Dhawan' , 3: 'Virat'}
# print(a.pop(1))
# print(a)

# a = { 1: 'Rohit' , 2: 'Dhawan' , 3: 'Virat'}
# a.popitem()
# print(a)


# keys=['Rohit','Dhoni','virat','Rishab Pant']
# values=['Mumabi','Chennai','RCB','Delhi']
# data = dict(zip(keys,values))
# print(data)

#duplicates not allowed
# dict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020
# }
# print(dict)

#nested dictionary
# ab = {'fruit':'apple','fruit':'mango','vegetable':{'onion','brinjal'}}
# print(ab['vegetable'])
# print(ab.values())
# print(ab)

#duplicate values
# a={'a':'23','n':'23','c':'45'}
# print(a)