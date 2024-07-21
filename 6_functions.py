# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

# create a function 
def sayHello(name):
    print(f'Hello {name}!')
sayHello("harsh")

# return values 
def getSum(num1,num2):
    sum= num1 + num2
    return sum
Sum = getSum(3,4)

# print 
print(
Sum
)



# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

# lambda func to add two numbers 
Sum2 = lambda num1,num2: num1 + num2
print(Sum2(1,2))

# another func 
hello = lambda: "Hello, world!"
print(hello())


