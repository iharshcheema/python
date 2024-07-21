# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name ='john'

# concatenate 
print('hello my name is ' + name )

# arguments by positions 
print('hello my name is {name}'.format(name=name))

# F-strings
print(f'Hello my name is {name} ')

# String Methods
s = 'hello world'

# capitalise 
print(s.capitalize())

# Make all uppercase
print(s.upper())

# Make all lower
print(s.lower())

# Swap case
print(s.swapcase())

# Get length
print(len(s))

# Replace
print(s.replace('world', 'everyone'))

# Count
sub = 'h'
print(s.count(sub))

# Starts with
print(s.startswith('hello'))

# Ends with
print(s.endswith('d'))

# Split into a list
print(s.split())

# Find position
print(s.find('r'))

# Is all alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())

