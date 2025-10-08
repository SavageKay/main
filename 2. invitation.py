#random Library with fxns for random selection.
from random import choice
names = ["Abraham Licolin", "Einstein", "Ghandi", "Columbus", "Rango", "M.J.", "Jason Statham"]
n = len(names)
for i in range(0,n,2):
    print(f"{names[i]} is not invited!")
for i in range(1,n,2):
    print(f"{names[i]} is invited!")
print("\n")
for i in range(0,n):
    print(f"{choice(names)} is invited!")
