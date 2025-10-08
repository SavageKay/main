# Shorthand If Statement
# This is a shorthand way to write an if statement
# It is useful for simple conditions where you want to assign a value based on a condition.
# value_if_true if condition else value_if_false
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
         None
for car in cars:
    print(car.upper()) if car == "bmw" else None

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

print("bmw" in cars and "ferari" in cars)