number = float(input())
inbound = input()
outbound = input()

number_in_meters = 0

if inbound == "mm":
    number_in_meters = number/1000
elif inbound == "cm":
    number_in_meters = number/100
elif inbound == "m":
    number_in_meters = number

if outbound == "mm":
    result = number_in_meters * 1000
elif outbound == "cm" :
    result = number_in_meters * 100

else:
    result = number_in_meters

print (f"{result:.3f}")
