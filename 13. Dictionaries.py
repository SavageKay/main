"""A dictionary in Python is a collection of key-value pairs. 
Each key is connected to a value, and you can use a key to 
access the value associated with that key. 
A key’s value can be a number, a string, a list, 
or even another dictionary. 
In fact, you can use any object that you can create in 
Python as a value in a dictionary."""

weapon = {'range': 'revolver', 'melee': 'knife', 'explosive': 'grenade'}

'''
print(weapon['range'])
print(weapon['melee'])

user_choice = input("Enter a weapon type (range, melee, explosive): ").lower()
if user_choice in weapon:
    print(f"You selected: {weapon[user_choice]}")
'''
# Adding a new key-value pair to the dictionary
weapon['magic'] = 'wand'
print(f"New weapon array: {weapon}")

# Starting with an empty dictionary
fav = {"game":"Call of Duty", "movie":"Infinity", "book":"Rich Dad Poor Dad"}
print(f"Original Favorite list: {fav}")

# Modifying an existing key-value pair
fav["movie"] = "Terminator"
print(f"My new favourite movie is: {fav['movie']}")

# Deleting a key-value pair
del fav["game"]
print(f"Updated Favorite list after deletion: {fav}")

pro_lang ={
    "Veron": "JavaScript",
    "Nisy" : "PHP",
    "Sandy": "Java",
    "Kwabena": "Python"
}
# Iterating through the dictionary
for name, language in pro_lang.items():
    print(f"{name} is a {language} developer.")

# Checking if a key exists in the dictionary
if "Nisy" in pro_lang:  
    print(f"Nisy is a {pro_lang['Nisy']} developer.")

# Using get() method to access a value
language = pro_lang.get("Kwabena", "Not Found")
print(f"Kwabena is a {language} developer.")