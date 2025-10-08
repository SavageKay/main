from datetime import date

current_year= date.today().year

def leap_year(current_year):
    print(f"Year: {current_year}")
    current_year = int(current_year)

    if (current_year % 4 == 0 and current_year % 100 != 0) or (current_year % 400 == 0):
        print(f"{current_year} is a leap year.")
    else:
        print(f"{current_year} is not a leap year.")

leap_year(current_year)

#Returning a Simple Value



