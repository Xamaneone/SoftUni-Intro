number = int(input())
for i in range(1, number + 1):
    num = str(i)
    num1 = num[0]
    num2 = 0
    try:
        num2 = num[1]
    except:
        hello_there = "hello_there"
    if int(num1) + int(num2) == 5 or int(num1) + int(num2) == 7 or int(num1) + int(num2) == 11:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")
# 5,7,11
