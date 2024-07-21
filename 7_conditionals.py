# If/ Else conditions are used to decide to do something based on something being true or false

x=4
y=20

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

# if 
if x > y :
   print(f'{x} is greater than {y}') 

# if  else-if else 
if x > y :
   print(f'{x} is greater than {y}') 
elif x == y :
   print(f'{x} is equal to {y}') 

else :
   print(f'{y} is greater than {x}') 

# nested if statements 
if x > 2 :
   if x <= 5:
      print(f'{x} is between 2 and 5')


# Logical operators (and, or, not) - Used to combine conditional statements

# and 
if x > 2 and x <= 5:
 print(f'{x} is between 2 and 5')
   

# or 
if x > 2 or x < 5:
   print(f'{x} is gretaer than 2 or less than 5')

#    not 
if not(x==y):
   print(f'{x} is not equal to {y}')


# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object

list =[1,2,3,4,5]
if x in list:
   print(f'{x} is in the list') 

# not in 
if x not in list:
   print(f'{x} is not in the list')


# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
if x is y:
   print(f'x is y')

if x is not y :
   print(x is not y)
#    this will return True 