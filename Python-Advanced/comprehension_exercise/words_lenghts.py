def name_with_lenght(name):
    return f"{name} -> {len(name)}"


data = input().split(", ")

result = [name_with_lenght(name) for name in data]

print(", ".join(result))
