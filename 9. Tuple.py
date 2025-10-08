"""A tuple looks just like a list, except you use parentheses 
 instead of square brackets. Once you define a tuple,
  you can access individual elements by using each item’s index,
 just as you would for a list.
 Tuples are immutable (cannot be changed)"""

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

"""Tuples are technically defined by the presence of a comma; 
the parentheses make them look neater and more readable.
If you want to define a tuple with one element, you
need to include a trailing comma"""
my_t = (3,)
print(my_t)

"""Although you can’t modify a tuple, you can
assign a new value to a variable that represents a tuple."""

print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
    
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)






