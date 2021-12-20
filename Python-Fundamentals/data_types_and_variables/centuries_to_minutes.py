number = int(input())
years = number * 100
days = years * 365.2422
days = int(days)
hours = days * 24
hours = int(hours)
minutes = hours * 60
minutes = int(minutes)
print(f"{round(number)} centuries = {round(years)} years = {round(days)} days = {round(hours)} hours = {round(minutes)} minutes")
