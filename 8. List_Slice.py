#4-10. Slices:
cubes =[num**3 for num in range(1,11)]
mid = len(cubes)//2
print(cubes)
print("The first three items in the list are:",cubes[:3])
print("Three items from the middle of the list are:",cubes[mid-1:mid+2])
print("The last three items in the list are:",cubes[-3:])

#4-11. My Pizzas, Your Pizzas: pg.103
pizzas = ["cheese","pepperoni","Hawaian"]

for pizza in pizzas:
    print(f"I like {pizza} pizza.")
friend_pizzas = pizzas[:]
pizzas.append("mushroom")
friend_pizzas.append("stuffed crust")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(f"{pizza.title()}")

print("My friend’s favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(f"{friend_pizza.title()}")