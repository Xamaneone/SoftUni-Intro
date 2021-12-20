def only_letters(temp):
    keywords = ['1', '2', '3', '4', '5', '6', '7', '8', '9', "-", "_"]
    for keyword in keywords:
        temp = temp.replace(keyword, "")
    return temp


def is_valid(user):
    if 3 <= len(user) <= 16 and only_letters(user).isalpha():
        return valids.append(user)
    return


valids = []
data = input().split(", ")

for username in data:
    is_valid(username)

for user in valids:
    print(user, end="\n")
