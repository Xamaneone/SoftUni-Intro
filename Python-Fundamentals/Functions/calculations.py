act = input()
first_num = int(input())
second_num = int(input())
def calculator():
    if act == "multiply":
        return first_num * second_num
    if act == "divide":
        return first_num / second_num
    if act == "add":
        return first_num + second_num
    if act == "subtract":
        return first_num - second_num

a = calculator()

print(int(a))