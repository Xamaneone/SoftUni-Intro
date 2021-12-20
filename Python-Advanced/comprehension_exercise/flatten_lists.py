data = list(input().split("|")[::-1])


data = [value.split() for value in data]

filtered_nums = [char for value in data for char in value]


print(*filtered_nums)

