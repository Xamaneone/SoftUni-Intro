command = input()
todo_list = []
while command != "End":
    todo_list.append(command)
    command = input()

todo_list.sort()
result = []
for todo in todo_list:
    temp = todo.split("-")
    result.insert(int(temp[0]), temp[1])
print(result)
