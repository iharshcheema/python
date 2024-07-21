# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# similar to Object in js 


# create a dictionary 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict, type(thisdict))

# get a value 
print(thisdict["brand"])
print(
    thisdict.get("brand")
)

# add a value 
thisdict['color']= "black"
print(thisdict)

# get dictionary keys 
print(thisdict.keys())

# get dictionary items 
print(
    thisdict.items()
)
# this will print: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964), ('color', 'black')])

# copy a dictionary and add a key value pair to the dictionary
car= thisdict.copy()
car['owner']='harsh'
print(car)
# this is something like spread operator in js 


# remove an item from the dictionary
del(thisdict['year'])
# thisdict.pop('year')
print(thisdict)

# clear
car.clear()
print(car)

# array of objects is list of dictionaries in python 
myList =[{
    'name': 'John',
    'age': 30,
    'city': 'New York'
} , {
     'name': 'Jessica',
    'age': 22,
    'city': 'New York'
}]
print(myList)

# this will print the first index of the list 
print(myList[1]['name'])



 