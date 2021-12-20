month = input()
hours = int(input())  #  5+ hours spent  = -50% from price per person
group = int(input())  #  4+ persons = price goes 10% per person down
time = input()
if month == "march" or month == "april" or month == "may":
    if time == "day":
        price = 10.50
    elif time == "night":
        price = 8.4
elif month == "june" or month == "july" or month == "august":
    if time == "day":
        price = 12.60
    elif time == "night":
        price = 10.20
if group >= 4:
    price = price * 0.9
if hours >= 5:
    price = price - (price * 0.5)

print(f"Price per person for one hour: {price:.2f}")
print(f"Total cost of the visit: {(price * group) * hours:.2f}")