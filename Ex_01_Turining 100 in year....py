import datetime
name = input("Please enter Your name: ")
#if len(name) < 1 : name = "Tala"
age = input("Please enter You age: ")
year = ((datetime.date.today().year - 100 + int(age)))
print(name, "You will turn 100 years in year", year)