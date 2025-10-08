from random import choice
#3-4
names = ["Kofi", "Yaw", "Elijah", "Randy",
          "Peter", "Joe", "Ama"]

for i in range(len(names)):
    print(f"{i+1}. {names[i].title()} is invited to dinner.")
print(f"There are {len(names)} invitations.\n")

#3-5  Changing Guest List:
print(f"{names[2]} can't make it.")

names[2] = "Kwame" #Replace
for i in range(len(names)):
    print(f"{i+1}. {names[i].title()} is invited to dinner.")
print(f"There are {len(names)} invitations.\n")

#3-6 More Guests:
print("I've found a bigger table, so there are more invitations available.")
names.insert(0, "Kwabena")
names.insert((len(names)+2)//2, "Daniel")
names.append("Leo")
for i in range(len(names)):
    print(f"{i+1}. {names[i].title()} is invited to dinner.")
print(f"There are {len(names)} invitations.\n")

#3-7 Shrinking Guest List
print("Bad news everyone, I can invite only two people for dinner.")

while len(names) > 2:
    uninvited = choice(names)  # randomly select a guest
    names.remove(uninvited)    # remove the selected guest
    print(f"Sorry {uninvited}, you're uninvited.")

    # Inform the remaining guests
for guest in names:
    print(f"{guest}, you're still invited!")

del names[:]
print("Guest list is now empty:", names)

