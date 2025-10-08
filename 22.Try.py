#Pg. 127
#7-8 Deli & 7-9 No Pastrami:
'''
sandwich_orders = [
    'tuna sandwich', 'club sandwich', 'pastrami sandwich',
    'avocado sandwich', 'chicken sandwich', 'pastrami sandwich', 
    'pastrami sandwich', 'egg sandwich', 
                   ]

print("Sorry, we are currently out of pastrami.")
finished_sandwiches = []

while sandwich_orders:
    if 'pastrami sandwich' in sandwich_orders:
        sandwich_orders.remove('pastrami sandwich')
    current_orders = sandwich_orders.pop()
    print(f"\n*Preparing {current_orders.title()}...")
    print(f"*Finished {current_orders.title()}")

    finished_sandwiches.append(current_orders)

print("\n--- Finished Orders ---")
for sandwich in finished_sandwiches:
        print(f"\t* {sandwich.title()}")
'''
#7-10. Dream Vacation:
pollActive = True
prompt = "\nIf you could visit one place in the world, \nwhere would you go?\n"
while pollActive:
     ask = input(prompt)
     print(f"\nChartering a flight to {ask.title()}✈... \nHave a nice time!👋🏼")
     pollActive = False


