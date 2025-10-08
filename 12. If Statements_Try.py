#5-3 Alien Colours 1
alien_color = "green"
if alien_color == "green":
    print("+ 5 points!")

#5-4 Alien Colours 2
alien_color = "red"
if alien_color == "green":
    print("(Green) + 5 points!")
else:
    print("(Red or Yellow) + 10 points!")

#5-5 Alien Colours 3
alien_color = input("Enter a color, red, yellow or green:")
if alien_color.lower() == "green":
    print("(Green) + 5 points!")
elif alien_color.lower() == "yellow":
    print("(Yellow) + 10 points!")
elif alien_color.lower() == "red":
    print("(Red) + 15 points!")

#5-6 Stages of Life:
age = int(input("Enter your age: "))
if age < 2:
    print("Stage of life: Baby")
elif 2 <= age < 4:
    print("Stage of life: Toddler")
elif 4 <= age < 13:
    print("Stage of life: Kid")
elif 13 <= age < 20:
    print("Stage of life: Teenager")
elif 20 <= age < 65:
    print("Stage of life: Adult")
elif 65 <= age:
    print("Stage of life: Elder")

#5-8. Hello Admin:
user_names = ["k2asav","","hello_kit","admin","my_pi","helsing"]
if len(user_names) == 0:
   print("We need to find some users!")
for name in user_names:
    if name == "admin":
       print("Hello admin, would you like to see a status report?") 
    else:
       print(f"Hello {name}, thank you for logging in again.") 

#5-9. No Users: 
if len(user_names) == 0:
    print("We need to find some users!")

del user_names[:]

#5-10. Checking Usernames:
current_users = ["k2asav", "hello_kit", "admin", "my_pi", "helsing"]

new_users = ["ello", "kpo","ishow", "k2asav", "My_pi", "akaza"]

lowcase_current_users = [user.lower() for user in current_users]

print("\nChecking new usernames:")
for new_user in new_users:
    if new_user in lowcase_current_users:
        print(f"{new_user} has already been taken, please enter a new name.")
    else:
        print(f"{new_user} is available for use.")

#5-11. Ordinal Numbers:
ordinal_nums = list(range(1,10))
for num in ordinal_nums:
    if num == 1:
        print("1st")
    elif num == 2:
        print("2nd")
    elif num == 3:
        print("3rd")
    else:
        print(f"{num}th")