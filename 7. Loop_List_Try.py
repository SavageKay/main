#4-3. Counting to Twenty:
for num in range(1,21):
    print(num)

#4-5. Summing a Million:
mill = []
for num in range(1,1000001):
    mill.append(num)
print(min(mill))
print(max(mill))
print(sum(mill))

#4-6. Odd Numbers:
odd = []
for num in range(1,21,2):
    odd.append(num)
print(odd)

#4-7. Threes:
mthrees = []
for num in range(3,31,3):
    mthrees.append(num)
print(mthrees)

#4-8. Cubes:
cube = []
for num in range(1,11):
    cube.append(num**3)
print(cube)

#4-9. Cube Comprehension:
cubes =[num**3 for num in range(1,11)]
print(cubes)

#Copying a List
"""When copying a list, use a slice."""
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print(friend_foods)
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:",my_foods)
print("\nMy friend's favorite foods are:",friend_foods)
