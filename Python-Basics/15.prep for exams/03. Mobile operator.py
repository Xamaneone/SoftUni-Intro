time = input()
type = input()
mobile_operator = input()
paying_months = int(input())
sum = 0
if time == "one":
    if type == "Small":
        sum += 9.98
        if mobile_operator == "yes":
            sum += 5.50
    elif type == "Middle":
        sum += 18.99
        if mobile_operator == "yes":
            sum += 4.35
    elif type == "Large":
        sum += 25.98
        if mobile_operator == "yes":
            sum += 4.35
    elif type == "ExtraLarge":
        sum += 35.99
        if mobile_operator == "yes":
            sum += 3.85
    sum = sum * paying_months
    print(f"{sum:.2f} lv.")
elif time == "two":
    if type == "Small":
        sum += 8.58
        if mobile_operator == "yes":
            sum += 5.50
    elif type == "Middle":
        sum += 17.09
        if mobile_operator == "yes":
            sum += 4.35
    elif type == "Large":
        sum += 23.59
        if mobile_operator == "yes":
            sum += 4.35
    elif type == "ExtraLarge":
        sum += 31.79
        if mobile_operator == "yes":
            sum += 3.85
    sum -= sum *0.0375
    sum = sum * paying_months
    print(f"{sum:.2f} lv.")