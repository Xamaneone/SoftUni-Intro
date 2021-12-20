import re

data = input()

names = []
total_price = 0

pattern = r"(^>>)(?P<name>\w+)<<(?P<price>\d+(\.\d+)?)\!(?P<quantity>\d+)"


while data != "Purchase":
    match = re.match(pattern, data)
    if match:
        obj = match.groupdict()
        names.append(obj["name"])
        total_price += float(obj["price"]) * int(obj["quantity"])
    data = input()


print(f"Bought furniture:")
for name in names:
    print(name)

print(f"Total money spend: {total_price:.2f}")