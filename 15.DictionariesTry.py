#6-5 Rivers:
rivers = {
    "Nile": "Egypt",
    "Amazon": "Brazil",
    "Yangtze": "China",
}

for river, country in rivers.items():
    print(f"The {river.title()} runs throught {country.title()}.")

print("\nThe following rivers are included in the dictionary:")
for river in rivers.keys(): 
    print("•",river.title())

print("\nThe following countries are included in the dictionary:")
for country in rivers.values():
    print("•",country.title())

#6-6. Polling:
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',       
    'edward': 'ruby',
    'phil': 'python'}

polls = ['jen', 'sasha', 'edward', 'phil', 'james', 'john']

for name in polls:
    if name in favorite_languages.keys():
        print(f"Thank you {name.title()} for taking the poll.")
    else:
        print(f"{name.title()}, please take our poll!")