#7-4. Pizza Toppings:
"""
prompt = "\nEnter your preferred pizza topping:"
active = True
while active:
    topping = input(prompt).strip().lower()
    print(f"I'll add {topping} to your pizza.")
    opt = input("Would you like to add another topping? (y/n): ").strip().lower()
    
    if opt == 'n':
        active = False
        print("Finished adding toppings to your pizza.")
"""

#7-5. Movie Tickets:
age_prompt = "\nEnter your age to determine your movie ticket price:"
active = True
while active:
    age_input = int(input(age_prompt).strip().lower())
    
    if age_input < 3:
        print("Your ticket is free.")
    elif age_input <= 12:
        print("Your ticket price is $10.")
    elif age_input > 12:
        print("Your ticket price is $15.")

    opt = input("Would you like to check another age? (y/n): ").strip().lower()
    if opt == 'n':
        active = False
        print("Exiting the ticket price checker.")

#7-6. Three Exits:
