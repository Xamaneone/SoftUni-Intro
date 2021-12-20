class parking:
    def __init__(self):
        self.data = {}

    def register(self, username, plate):
        if username in self.data:
            return f"ERROR: already registered with plate number {plate}"
        self.data[username] = plate
        return f"{username} registered {plate} successfully"

    def unregister(self, username):
        if username not in self.data:
            return f"ERROR: user {username} not found"
        self.data.pop(username)
        return f"{username} unregistered successfully"

counter = int(input())

Parking = parking()
for _ in range(counter):
    data = input().split(" ")
    if data[0] == "register":
        print(Parking.register(data[1], data[2]))
    else:
        print(Parking.unregister(data[1]))

for name, plate in Parking.data.items():
    print(f"{name} => {plate}")
