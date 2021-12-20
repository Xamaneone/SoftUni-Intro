company = {}

data = input()

while not data == "End":
    name, id = data.split(" -> ")
    if name not in company:
        company[name] = [id]
    else:
        if id not in company[name]:
            company[name].append(id)

    data = input()


for name, id in sorted(company.items()):
    print(f"{name}")
    for ID in id:
        print(f"-- {ID}")