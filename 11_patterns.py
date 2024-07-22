n = 5
# box pattern 
# for i in range(n):
#  for j in range(n):
#      print('*' , end=" ")
#  print()

# increasing triangle pattern 
# for i in range(n):
#    for j in range(i+1):
#       print('*' , end=" ")
#    print()  

# decreasing triangle pattern 
# for i in range(n):
#    for j in range(i,n):
#       print("*" , end =" ") 
#    print()   

#right triangle
# for i in range(n):
#     for j in range(i,n):
#         print("a" , end =" ")
#     for k in range(i+1):
#         print("*", end=" ")
#     print()

# left triangle
# for i in range(n):
#     for j in range(i+1):
#      print("a", end = " ")  
#     for j in range(i,n):
#      print("*", end = " ")
#     print() 

# hill pattern 
# for i in range(n):
#  for j in range(i,n-1):
#   print(" ", end = " ") 
#  for k in range(i) :
#   print("*", end = " ")
#  for l in range (i+1):
#   print("*", end = " ")
#  print()    

# reverse hill pattern 
# for i in range(n):
#  for j in range(i):
#   print("a", end = " ")
#  for k in range(i,n-1): 
#   print("*" , end = " ")
#  for l in range(i,n):
#   print("*" , end = " ") 
#  print() 
  
# hourglass pattern 
for i in range(n - 1):
    for j in range (i):
        print("a" , end="")
    for k in range(i, n):
        print("*", end=" ")   
    print()    

for i in range(n):
    for j in range(i,n-1) :
        print("a" , end="")
    for k in range(i+1):
        print("*", end=" ")    
    print()    












