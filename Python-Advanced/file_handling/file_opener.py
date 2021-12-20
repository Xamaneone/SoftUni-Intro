try:
    with open("File Opener/text.txt", "r") as file:
        print("File found!")
except FileNotFoundError:
    print("File not found")