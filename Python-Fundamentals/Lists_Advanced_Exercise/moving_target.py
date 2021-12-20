targets = input().split(" ")
targets = list(map(int, targets))
data = input()

def shoot(nums, i, v):
    if 0 <= i < len(nums):
        nums[i] -= v
        if nums[i] <= 0:
            nums.pop(i)
    return nums

def add_target(nums, i, v):
    if 0 <= i < len(nums):
        nums.insert(i, v)
    else:
        print("Invalid placement!")
    return nums

def strike(nums, i, r):
    if 0 <= i - r < i + r < len(nums):
        for index in range(i-r, i+r+1):
            nums.pop(i-r)
    else:
        print("Strike missed!")
    return nums




while not data == "End":
    command, index, value = data.split(" ")
    index = int(index)
    value = int(value)

    if command == "Shoot":
        targets = shoot(targets, index, value)
    elif command == "Add":
        targets = add_target(targets, index, value)
    elif command == "Strike":
        targets = strike(targets, index, value)


    data = input()

print("|".join([str(el) for el in targets]))