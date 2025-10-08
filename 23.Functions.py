# def informs Python that you’re defining a function.

def greet_user(username): 
 """Display a simple greeting."""
 print(f"Hello, {username.title()}!")
greet_user('jesse')

#---Function definition---
 # Function definition tells Python the name of the function
 # and, if applicable, what kind of information the function
 #  needs to do its job.


#---Arguments and Parameters---
#-------------------------------
# 'username' is a parameter, 
# a piece of information the function needs to do its job.
#--------------------------------------
# 'jesse' is an argument, a piece of information that’s 
# passed from a function call to a function. 


#8-1. Message:
def display_message():
    """Display a simple message."""
    print("I am learning about functions in Python.🐍")

display_message()

#8-2. Favorite Book:
def favorite_book(title):
    """Display a message about someone's favorite book."""
    print(f"One of my favorite books is '{title.title()}'.📚")

favorite_book('atomic habits')

# Passing Arguments
#-------------------
# Positional Arguments
# In a fundtion call, the number and order of the arguments
# must match the parameters in the function definition.
def full_name(first_name, last_name):
    """Display a full name."""
    full_name = f"{first_name} {last_name}"
    print(f"Full name: {full_name.title()}")

full_name('Chris', 'Hemsworth')
#-----------------------------------

# Keyword Arguments
# A keyword argument is a name-value pair that you pass to a function.
# You directly associate the name and the value within the argument,
# so when you pass the argument to the function, there’s no confusion.
full_name(last_name='Evans', first_name='Chris')

#Default Values
# If an argument is missing in the function call, Python uses the
# default value 'if' specified in the function definition.

def weather(city='New Jersey', weather='sunny'):
    """Display the weather in a city."""
    print(f"The weather in {city} is {weather}.")

print("--- Default Values ---")
weather()
#Output: The weather in 'New Jersey' is 'sunny'.

print("\n--- Positional Arguments ---")
weather('London')
#Output: The weather in 'London' is sunny.

print("\n--- Keyword Arguments ---")
weather(weather='cloudy')
#Output: The weather in 'New Jersey' is 'cloudy'.

print("\n---Positional ---")
weather('Tokyo', 'rainy')
#Output: The weather in 'Tokyo' is 'rainy'.

#NOTE:
#When you use default values, any parameter with a 
# default value needs to be listed after all
#  the parameters that don’t have default values.
#  This allows Python to continue interpreting 
# positional arguments correctly.

#8-3. T-Shirt:
def make_shirt(size, message):
    """Display a message about a shirt."""
    print(f"The shirt size is {size}, \nand the message is '{message}'.")

make_shirt('Large', 'I\'m a millionaire!💰') # Positional
make_shirt(size='Medium', message='Python is awesome!') #Keyword