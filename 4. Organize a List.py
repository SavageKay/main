# sort() method changes the order of the list permanently
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() #Alphabetical order
print("Alphabetical Order:",cars)
cars.sort(reverse=True) #Reverse Alphabetical
print("Reverse Alphabetical Order:",cars)

""" sorted method function lets you display your list
    in a particular order, but doesn’t affect the actual 
    order of the list.
"""
print("\n")
print("Original: ",cars)
print("Sorted: ",sorted(cars))
print("Original again: ",cars)

#Reverse Order
#The reverse() method changes the order of a list permanently
print("\nReverse Order:")
cars.reverse()
print(cars)