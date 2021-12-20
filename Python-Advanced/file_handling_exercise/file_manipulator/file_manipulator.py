import os


def create_file(file_name):
    with open(f"{file_name}", "w"):
        pass


def add_content_to_file(file_name, content):
    with open(file_name, "a") as file:
        file.write(f"{content}\n")



def replace_content_in_file(file_name, old_content, new_content):
    if not os.path.exists(file_name):
        print(f"An error occurred")
        return
    with open(file_name, "r") as file:
        file_data = file.read()

    file_data = file_data.replace(old_content, new_content)

    with open(file_name, "w") as file:
        file.write(file_data)


def delete_file(file_name):
    if not os.path.exists(file_name):
        print(f"An error occurred")
        return
    os.remove(f"{file_name}")






command = input()
while command != "End":
    if command.startswith("Create"):
        temp, name = command.split("-")
        create_file(name)
    elif command.startswith("Add"):
        temp, name, content = command.split("-")
        add_content_to_file(name, content)
    elif command.startswith("Replace"):
        temp, name, old, new = command.split("-")
        replace_content_in_file(name, old, new)
    elif command.startswith("Delete"):
        temp, name = command.split("-")
        delete_file(name)
    command = input()