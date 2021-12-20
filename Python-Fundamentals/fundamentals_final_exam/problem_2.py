import re

count = int(input())

pattern = r"(U\$)(?P<username>[A-Z][a-z]{2,})\1(P@\$)(?P<password>[a-zA-Z]{5,}\d+)\3"

successful = 0

for _ in range(count):
    line = input()
    match = re.match(pattern, line)
    if match:
        obj = match.groupdict()
        print(f"Registration was successful")
        print(f"Username: {obj['username']}, Password: {obj['password']}")
        successful += 1
        continue
    print(f"Invalid username or password")

print(f"Successful registrations: {successful}")

