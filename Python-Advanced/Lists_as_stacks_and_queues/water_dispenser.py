from _collections import deque


START_COMMAND = "Start"
END_COMMAND = "End"
REFILL_COMMAND = "refill"
water_in_dispenser = int(input())

peoples_queue = deque()
while True:
    command = input()
    if command == START_COMMAND:
        break
    peoples_queue.append(command)

while True:
    command = input()
    if command == END_COMMAND:
        print(f"{water_in_dispenser} liters left")
        break
    elif command.startswith(REFILL_COMMAND):
        command_params = command.split(" ")
        refill_liters = int(command_params[1])
        water_in_dispenser += refill_liters
        continue
    else:
        person = peoples_queue.popleft()
        person_liters = int(command)
        if person_liters <= water_in_dispenser:
            print(f"{person} got water")
            water_in_dispenser -= person_liters
        else:
            print(f"{person} must wait")