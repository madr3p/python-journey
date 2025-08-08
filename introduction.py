# TOP CODERS MALAYSIA WORKSHOP - Python Concepts with Simplified Explanations and Scenarios

# google colab : https://colab.research.google.com/drive/1zPVN-eBZ76WJGqKpLVZMM-hvxD7nOccs?usp=sharing
# ebox : https://pro.e-box.co.in/participant/home
# INTRODUCTION
# Computers follow instructions, but they don't understand human language or numbers directly.
# We use a programming language (like Python), and a compiler translates our code into binary for the computer.

# A good programmer knows:
# 1. How to write code using correct syntax (language knowledge)
# 2. How to solve problems with clear logic (problem-solving skill)



# 1. BASIC INPUT/OUTPUT EXAMPLE
# Scenario: Simple calculation - multiply two numbers
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
result = x * y
print("Result:", result)

# Input: 5, 8
# Output: Result: 40



# 2. LITERALS AND DATA TYPES
# Literal = actual data (e.g. 10, "apple", 3.14, True)
# Python has 4 basic literal types: string, integer, float, boolean
print("Television")   # String literal
print(10)             # Integer literal
print(1455.55)        # Float literal
print(True)           # Boolean literal

# Use type() to check the data type of a literal:
print(type("Hello"))  # <class 'str'>
print(type(10))       # <class 'int'>
print(type(1455.55))  # <class 'float'>
print(type(True))     # <class 'bool'>



# 3. VARIABLES
# Variables store values. Python assigns the type automatically based on the value.
product = "Television"
quantity = 10
price = 1455.55
isAvailable = True

print("Product:", product)
print("Quantity:", quantity)
print("Price:", price)
print("Available:", isAvailable)

# Check the memory address of a variable using id():
print(id(product))



# 4. TYPE CASTING (Changing data type)
x = "10"
y = "15"
print(x + y)  # "1015" (string)

x = int(x)
y = int(y)
print(x + y)  # 25 (integer addition)



# 5. OPERATOR BEHAVIOR
product = "Book"
repeat = 3
print(product * repeat)  # BookBookBook


# 6. BOOLEAN CONVERSION
print(bool(0))       # False
print(bool(123))     # True
print(bool(""))      # False (empty string)
print(bool("Hi"))    # True (non-empty string)



# 7. NONE TYPE
# Use None to represent 'no value yet'
x = None
print(x)             # None
print(type(x))       # <class 'NoneType'>



# 8. MULTIPLE ASSIGNMENTS
# Assign same value to multiple variables
home = office = "water"
print(home, office)

# Assign many values to one variable (as a list)
fruits = ["apple", "mango", "banana", "grapes"]
print(fruits)

# Accessing list items
print(fruits[0])      # apple
print(fruits[-1])     # grapes
print(fruits[1:3])    # ['mango', 'banana']
print(fruits[::-1])   # reverse list

# Unpack list into separate variables
f1, f2, f3, f4 = fruits
print(f1, f2, f3, f4)

# Tuples (like lists but read-only)
tuple_fruits = ("apple", "orange", "mango")
print(tuple_fruits[1])  # orange



# 9. STRINGS AS CHARACTER LISTS
message = "Welcome"
print(message[0])     # W
print(message[::-1])  # emocleW



# 10. OBJECTS AND CLASSES
# Every data type in Python is an object from a class
x = 10
print(x, type(x))  # <class 'int'>

x = 1455.55
print(x, type(x))  # <class 'float'>

x = "Hello"
print(x.upper())   # HELLO
print(x.lower())   # hello
print(x.count("l"))  # count of 'l'
print(len(x))        # number of characters



# 11. LIST METHODS
fruits = ["apple", "apple", "orange", "mango", "banana", "apple", "grapes"]
fruits.append("durian")
print(fruits.count("apple"))  # 3

# Remove 3 apples (only removes the first match each time)
fruits.remove("apple")
fruits.remove("apple")
fruits.remove("apple")

# Replace "grapes" with "mangosteen"
i = fruits.index("grapes")
fruits[i] = "mangosteen"

# Insert at specific position
fruits.insert(4, "papaya")

# Sort and reverse the list
fruits.sort()
fruits.reverse()
print(fruits)

# JOIN and SPLIT
characters = ["P", "y", "t", "h", "o", "n"]
print("".join(characters))     # Python
print("-".join(characters))    # P-y-t-h-o-n

msg = "Welcome to python"
print(msg.split())             # ['Welcome', 'to', 'python']



# 12. USER INPUT + TYPE CONVERSION
# Scenario: Calculate simple interest
principle = input("Enter principle amount (RM): ")
period = input("Enter period (in years): ")
rate = input("Enter interest rate (%): ")

# Convert inputs to appropriate types
principle = int(principle)
period = int(period)
rate = float(rate)

simple_interest = (principle * period * rate) / 100
print("Interest Amount:", simple_interest)

# Input:
# Enter principle amount (RM): 1000
# Enter period (in years): 2
# Enter interest rate (%): 5.5
# Output:
# Interest Amount: 110.0



# 13. OPERATORS

# Arithmetic operators
x = 10
y = 5
z = 4
print(x + y) # 15 addition
print(x - y) # 5 subtraction
print(x * y) # 50 multiplication
print(x / y) # 2.0, division will always result in float (with decimals)
print(x // z) # 2 x 4 = 8, quotient is 2
print(x % z) # 10 - 8 = 2, remainder

x = 20
y = 5
z = 6
print(x + y) # 25 addition
print(x - y) # 15 subtraction
print(x * y) # 100 multiplication
print(x / y) # 2.0, division will always result in float (with decimals)
print(x // z) # 3 x 6 = 18, quotient is 3
print(x % z) # 20 - 18 = 2, remainder

# Comparison Operators
x = 10
y = 5
z = 10
#Create True statements using various comparison operators
print(x > y) # True 
print(y < x) # True
print(x == z) # True
print(x != y) # True
print(x >= y) # True
print(x <= y) # True

# Logical operators
# - Used whenever we want to compare more than 1 condition
# I want to book a hotel. My budget per night is RM150. I am looking for 3 stars and above

# My criteria
myBudget = 150
requiredStars = 3
# Hotel data
hotel_Price = 145
hotel_Stars = 4
print(hotel_Price <= myBudget and hotel_Stars >= requiredStars) # True
# The first condition returns True and the second condition returns True
# We are using and operator both condition must return True then only the whole expression will return True

# I want to buy Television. My budget for non-branded television is 1500. I dont mind spending any amount for branded television

# My criteria
non_branded_budget = 1500

# Television data
tv_one_brand = None
tv_one_price = 1450.25
tv_two_brand = "Sony"
tv_two_price = 1950.75
tv_three_brand = "LG"
tv_three_price = 5150.25

print((tv_one_brand is None and tv_one_price <= non_branded_budget) or (tv_one_brand is not None)) # False
# The first condition returns True and the second condition returns False
# We are using or operator either one condition is True this will  True

print((tv_two_brand is None and tv_one_price <= non_branded_budget) or (tv_two_brand is not None)) # True
# The first condition returns False and the second condition returns True
# We are using or operator either one condition is True this will  True

# To make decisions we always use comparison operators
# If I am hungry then I will have heavy breakfast else I will go for a coffee.
# (status == "Hungry") then "Heavy breakfast" else "Go for coffee"
print("Heavy Breakfast")
print("Go for coffee")
# However we do not want both statement to be executed
# So far whatever statement we have written all are executed
# Now either one print statement only will be executed
# First step create block of code
# You can create blocks using indentation (tab) and colon :
hungry = False # / True
if (hungry == True):
    # FIrst block of code
    print ("Heavy Breakfast")
else:
    # Second block of code
    print("Go for coffee")
# Go for coffee

# Find whether the given number is even or odd
givennumber = 5
# What to do? Divide the givennumber by 2 and if the remainder is 1 then givennumber is odd
# What to do? Divide the givennumber by 2 and if the remainder is 0 then givennumber is even
# How to do?
remainder = givennumber % 2
if remainder == 1:
    print("Given number", givennumber)
    print("Is Odd number")
else:
    print("Given number", givennumber)
    print("Is Even number")
# Given number 6
# Is Even number

# Find whether the given number is positive or negative
givennumber = 9
# What to do? If the givennumber is greater than or equal to 0 then givennumber is positive
# What to do? If the givennumber is less then 0 then givenumber is negative
# How to do?
if givennumber >= 0:
    print("Given number", givennumber)
    print("is Positive")
else:
    print("Given number", givennumber)
    print("is Negative")
# Given number 9
# is Positive

# What is you want to make decisions based on more than 2 conditions
# Find whether the given number is positive, negative or zero

givennumber = 0
if givennumber >= 0:
    if givennumber == 0: # This statement is inside the outer if so there is 1 tab
        print("Given number", givennumber) # This statement is inside the innner if so there is 1 tab
        print("is Zero")
    else:
        print("Given number", givennumber)
        print("is Positive")
else:
    print("Given number", givennumber)
    print("is Negative")
# Given number 0
# is Zero

givennumber = 1
if givennumber >= 0:
    if givennumber == 0:
        print("Given number", givennumber)
        print("is Zero")
    else:
        print("Given number", givennumber)
        print("is Positive")
else:
    print("Given number", givennumber)
    print("is Negative")
# Given number  1
# is Positive

givennumber = -1
if givennumber >= 0:
    if givennumber == 0:
        print("Given number", givennumber)
        print("is Zero")
    else:
        print("Given number", givennumber)
        print("is Positive")
else:
    print("Given number", givennumber)
    print("is Negative")
# Given number  -1
# is Negative

# In Python they came up with another syntax if elif
givennumber = 0
if givennumber > 0:
    print("Given number", givennumber)
    print("is Zero")
elif givennumber == 0:
    print("Given number", givennumber)
    print("is Positive")
elif givennumber < 0:
    print("Given number", givennumber)
    print("is Negative")
# Given number 0
# is Zero

# Do we have to create block of code every time?
# If the statement to be executed is single line then no need to create block of code
x = 5
# Say it in english and type using python keyword you will get it right
print("Even") if (x % 2 == 0) else print ("Odd")
# Odd

# What if i have more than 2 condition
# Find whether the given number is positive, negative or zero
x = 5
print("+ve") if x > 0 else print("-ve") if x < 0 else print("Zero")
# +ve

# So far we have seen print statements are used inside the if block
# How about expressions inside the if else block
# Create a simple calculator
# if the operator is + the do addition
# if the operator is - then do subtraction
# if the operator is * then do multiplication
# if the operator is / then do division
# and return the result
x = 10
y = 5
op = "+"
result = x + y if op == "+" else x - y if op == "-" else x * y if op == "+" else x / y
print(result)
# 15

x = 10
y = 5
op = "-"
result = x + y if op == "+" else x - y if op == "-" else x * y if op == "+" else x / y
print(result)
# 5

x = 10
y = 5
op = "*"
result = x + y if op == "+" else x - y if op == "-" else x * y if op == "+" else x / y
print(result)
# 50

x = 10
y = 5
op = "/"
result = x + y if op == "+" else x - y if op == "-" else x * y if op == "+" else x / y
print(result)
# 2.0 - / will always return a float value



# 14. LOOP

# If you have a list with small number of items you can select the items using index
# If you have a list with large number of items and if you want to perform some kind of operation on the list then selecting the items using index is not practical
# We have to go for Loop

celciusvalues = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# We want to print the farenheit values
for celciusvalue in celciusvalues:
    farenheitvalue = (celciusvalue * 9/5) + 32
    print(celciusvalue, farenheitvalue)

# 0 32.0
# 1 33.8
# 2 35.6
# 3 37.4
# 4 39.2
# 5 41.0
# 6 42.8
# 7 44.6
# 8 46.4
# 9 48.2 
