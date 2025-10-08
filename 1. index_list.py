motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']

#del statement for when you know the position of the item
del motorcycles[1], motorcycles[2]

#The pop() method removes the item, but it lets you work with that item afterwards
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

#.remove() is just like pop() but if you only know the value of the item you want to remove
too_expensive = motorcycles.pop(-1)
print(f"A {too_expensive.title()} is too expensive for me.")

print(motorcycles)