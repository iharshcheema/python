# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

# for loop 
people =["john" , "sarah" , "harsh"] 

for item in people:
    print(f'current item is : {item}')

   
# break
#  we basically stops the loops if the item is sarah 
for item in people:
    if item == "sarah":
        break
    print(f'current Item is : {item}')

# continue 
# it skips the sarah item in the loop 
for item in people:
    if item == "sarah":
        continue
    print(f'current item is : {item}')

# range 
for item in range(len(people)):
    print(f' current Item is : {people[item]}')

# custom ranges 
for item in range(0,10) :
    print(f'current number is : {item}')
 



# While loops execute a set of statements as long as a condition is true.

count = 0
while count <=10:
    print(f'count is {count}')
    count = count + 1 
    # or count +=1
    