# Focusing on multiple multple user inputs in while loops
# using lists and dictionaries

"""Moving items from list to list"""
unconfirmed_users = ['alice','brian','collin', 'dave']
confirmed_users = []

#Verifying each user
while unconfirmed_users:
    current_user = unconfirmed_users.pop() 
    #pop() removes last item from list for use but it doesn't delete it permanently
    
    # Simulate verifying user add to confirmed list
    print(f"* Verifying user: {current_user.title()}....")
    print(f"* User '{current_user.title()}' verified\n")
    confirmed_users.append(current_user)
    #append() adds item to end of list

#Display all confirmed users
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print("\t* " + confirmed_user.title())

# Removing all instances of specific values from a list
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print("\nOriginal list of pets:")
print(pets)

while 'cat' in pets:
    pets.remove('cat')
    #remove() removes first instance of value from list

print("\nList of pets after removing all 'cat' instances:")
print(pets)

# Filling a dictionary with user input
responses = {}
#Set a flag to indicate that polling is active
polling_active = True

while polling_active:
    #Prompt the user for name and response
    fname = input("\nWhat is your first name? ").strip().title()
    response = input("Which mountain would you like to climb someday? ").strip().title()

    #Store the responses in the dictionary
    responses[fname] = response

    #Find out if anyone else is going to take the poll
    repeat = input("Would you like to let another person respond? (y/n) ").strip().lower()
    if repeat == 'n':
        polling_active = False
    
#Polling is complete. Show results
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")



