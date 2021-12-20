def fill_phonebook():
    data = input()
    phonebook = {}
    while not data.isdigit():
        name, number = data.split("-")
        phonebook[name] = number
        data = input()
    return phonebook, int(data)


def search_contact(contact_name, phonebook):
    if phonebook.get(contact_name):
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")


phonebook, iterations_count = fill_phonebook()

for _ in range(iterations_count):
    name = input()
    search_contact(name, phonebook)