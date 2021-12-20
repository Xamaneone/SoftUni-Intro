temp = input().split(", ")
data = [int(data) for data in temp]
max_num = max(data)
for num in range(10, max_num + 10, 10):
    nums_in_range = list(filter(lambda x: num >= x ,data))
    data = list(filter(lambda x: x > num ,data))
    print(f"Group of {num}'s: {nums_in_range}")
