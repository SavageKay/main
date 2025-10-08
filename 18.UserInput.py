# input() function interprets user input as a string
name = input("Please enter your name: ")
age = input("Enter your age: ")
print(f"Data Type: {type(name)}")
print(f"Data Type: {type(age)})")


# To get numerical input, convert the string to an integer or float
#age = int(input("Enter your age: "))
print(f"You will be {int(age) + 1} years old next year.")

height = float(input("Enter your height in meters: "))
print(f"You are {height} meters tall.")

#7-2. Restaurant Seating
num = int(input("How many people are in your dinner group? "))
if ValueError:
    print("Please enter a valid number.")
elif num > 8:
    print("You'll have to wait for a table.")
else:
    print("Your table is ready.")

#7-3. Multiples of Ten
num = int(input("Enter a number: "))
if num % 10 == 0:   
    print(f"{num} is a multiple of 10.")
else:
    print(f"{num} is not a multiple of 10.")

