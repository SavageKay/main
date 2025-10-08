#Nesting
# You can store multiple dictionaries in a list, or a list of
# items as a value in a dictionary.
aliens = []

for alien in range(30):
    new_alien = {"color": "green", 'points' : 5, 'speed' : 'slow'}
    aliens.append(new_alien)

# Modify the first 3 aliens
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'


# Show the first 7 aliens
print("The first 7 aliens are:")
for alien in aliens[:7]:
    print(alien)

print("...")

# Show how many aliens have been created
print(f"Total number of aliens: {len(aliens)}")


#List in a dictionary
pizza = {
    'crust': 'thick',
    'toppings': ['olives', 'extra cheese'],
}

# Summarize the order
print(f"You ordered a {pizza["crust"]}-crust pizza with: ")

for topping in pizza['toppings']:
    print(f"\t• {topping}")

#Dictionary in a dictionary
users = {
    'leo':{
        'first': 'lionel',
        'last': 'messy',
        'location': 'argentina',
                },

    'christian':{
        'first': 'christiano',
        'last': 'ronaldo',
        'location': 'portugal',
                },
}
for username, user_info in users.items():
    print(f"\nUsername: {username.title()}")
    full_name = f"{user_info['first'].title()} {user_info['last'].title()}"
    location = user_info['location'].title()

    print(f"\tFull name: {full_name}")
    print(f"\tLocation: {location}")