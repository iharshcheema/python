# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

#  create a class 
class User:
    # constructor
    def __init__(self ,name):
        # properties
        self.name = name
        self.email = 'johndoe@example.com'
        self.password = 'password123'

# method 
    def greeting(self):
            return f'Hi my name is {self.name}'
            
   
# initialise user object 
brad = User("Brad Traversy")
print(brad.greeting())





# Extend a class 
class Customer(User):
      def __init__(self ,name):
        # properties
        self.name = name
        self.email = 'johndoe@example.com'
        self.password = 'password123'
        self.balance=0
# method
      def setBalance(self,balance):
           self.balance = balance

# initialise Customer object 
harsh = Customer('harsh')

# change the  balance  using method 
harsh.setBalance(5000)

print(f'my name is {harsh.name} and my balance is {harsh.balance}')
      

