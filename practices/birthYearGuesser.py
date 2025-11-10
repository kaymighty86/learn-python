import datetime as dt

birth_year = int(input("What is your birth year?"))

age = dt.datetime.now().year - birth_year

print(f"Your are {age} years old!")