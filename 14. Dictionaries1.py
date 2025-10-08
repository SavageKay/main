#6-1. Person
client = {
    'first_name': 'Yaw',
    'last_name': 'Omah',
    'age': 24,
    'city': 'Accra'
}

for key, value in client.items():
    print(f"{key}: {value}")

#6-2. Fav Numbers:
fav_nums ={
    "Kay": 7,
    "Yaw": 9,
    "Appiah": 15,
    "Remy": 23,
    "Bob": 32
}
for name in fav_nums:
    print(name)
for name, number in fav_nums.items():
    print(f"{name}'s favorite number is {number}.")

#6-3. Glossary:
glossary = {
    "dictionary": "A collection of key-value pairs.",
    "list": "An ordered, mutable collection of items.",
    "tuple": "An immutable ordered collection of items.",
    "set": "An unordered collection of unique items.",
    "function": "A block of reusable code that performs a specific task."
}
for word, meaning in glossary.items():
    print(f"{word.title()}: {meaning}")


family = {
    'mother' : {
        'name' : 'Abena',
        'age'  : '46',
        'job'  : 'Social Worker'
    },
    'father' : {
        'name' : 'Kwame',
        'age'  : '49',
        'job'  : 'NHIS'
    },
    'brothers':{
        'name1': 'Jerry',
        'name2': 'Jayden',
        'age'  : '1',
        'job'  : 'None'
    }
}

for x , y in family.items():
    print ('\n*',x.title(),':')

    for obj in y:
        print(f"\t {obj.title()} : {y[obj]}")


#sorted() function gives a sorted list of the keys in the dictionary
print("\nSorted keys in the family dictionary:")    
for key,value in sorted(family.items()):
    print(key.title() + " : " + str(value))