"""Looping allows you to take the
 same action, or setof actions, with 
 every item in a list"""

#4-1. Pizzas:
pizzas = ['cheese', 'hawaian', 'pepperoni']
for pizza in pizzas:
 print(f"I like {pizza.title()} pizza!")

for value in range(1, 5):
 print(value)

even_numbers = list(range(2, 11, 2)) #range(start, stop, step)
print(even_numbers)

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

#List Comprehensions Pg. 98
squares = [value**2 for value in range(1, 11)]
print(squares) 

# Working with Part of a List
# Slicing a List
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[:3])
print(players[::2]) #list = [start:stop:step]
print(players[3:5])
print(players[2:-1])
print(players[2:])
print(players[-3:])
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
