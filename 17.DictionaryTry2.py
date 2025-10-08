#6-7 People
people = [
    {
        'first_name': 'Yaw',
        'last_name': 'Omah',
        'age': 24,
        'city': 'Accra'
    },

    {
        'first_name': 'Appiah',
        'last_name': 'Ofori',
        'age': 30,  
        'city': 'Kumasi'
    },
    
    {
        'first_name': 'Remy',   
        'last_name': 'Adjei',
        'age': 26,
        'city': 'Takoradi'
    }
]

for person in people:
    full_name = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = person['age']
    city = person['city'].title()
    print(f'{full_name} is {age} years old and lives in {city}.')


#6-8 Pets
    pets = [
        {   'type': 'dog',
            'owner': 'jack' },

        {   'type': 'parrot',
            'owner': 'perry' },
        
        {   'type': 'snake',
            'owner': 'andy' },

        {   'type': 'hamster',
            'owner': 'mike' },
        
        {   'type': 'cat',
            'owner': 'raul' }
    ]

for pet in pets:
    pet_type = pet['type'].title()
    owner = pet['owner'].title()
    print(f"{owner} owns a {pet_type}.")

#6-9 Favorite Places
favorite_places = {
    'leo': ['paris', 'new york', 'london'],
    'christian': ['madrid', 'manchester'],
    'nana': ['accra'],
    'yaw': []
}

for name, places in favorite_places.items():
    if len(places) > 1:
        print(f"\n{name.title()}'s favorite places are:")
        for place in places:
            print(f"\t• {place.title()}")
    elif len(places) == 1:
        print(f"\n{name.title()}'s favorite place is:")
        for place in places:
            print(f"\t• {place.title()}")
    else:
        print(f"\n{name.title()} has no favorite places listed.")
    

#6-10 Favorite Numbers

