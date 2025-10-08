prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""

#Using break to exit a loop
while message != 'quit':
    message = input(prompt).strip().lower()
    # only print if the user didn't request to quit
    if 'quit' in message:
        print("Exiting the program. Goodbye!")
        break
    print(message)

#Using a Flag
active = True
while active:
    message = input(prompt).strip().lower()
    # only print if the user didn't request to quit
    if 'quit' in message:
        print("Exiting the program. Goodbye!")
        active = False
    else:
        print(message)

#Using continue in a loop
# 'continue' statement tells Python to skip current iteration
# and move to the next iteration in the loop
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

 