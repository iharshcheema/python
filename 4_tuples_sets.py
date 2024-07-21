# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
# create a tuple 
names = ('harsh' , "john")

print(names , type(names))

# get a value 
print(names[1])


# length 
print(len(names))

# delete tuple 

# del names
# print(names)

# does not allow changing  of values 

# names[0]= 'scout'


# SETS 
# A Set is a collection which is unordered and unindexed. No duplicate members.

# create a set 
fruits= {'apples' , 'banans' , 'mangoes'}

print(fruits , type(fruits))

# check if in set 
print('apples' in fruits)

# add to set 
fruits.add('blueberry')
print(fruits)

# add duplicate 
fruits.add('apples')
print(fruits)

# remove 
fruits.remove('apples')
print(fruits)

# clear 
fruits.clear()
print(fruits) # returns empty set

# delete 
del fruits

# print(fruits) # this will raise an error because set is deleted








