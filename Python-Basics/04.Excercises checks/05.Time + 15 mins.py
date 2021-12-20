hours = int(input()) * 60
minutes = int(input())

all = hours + minutes + 15
hours = all // 60
minutes = all % 60

if hours > 23:
    hours = hours - 24

if minutes < 10:
    print (f"{hours}:0{minutes}")
else:
    print (f"{hours}:{minutes}")
