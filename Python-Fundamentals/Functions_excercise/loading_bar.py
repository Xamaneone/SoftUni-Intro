def loading_bar(number):
    just = True
    if number == 100:
        print("100% Complete!")
        print("[%%%%%%%%%%]")
        just = False
    if just is True:
        print(f"{number}%", end=" [")
        if just is True:
            number = number // 10
        for num in range(1, number+1):
            print("%", end="")
        for num in range(number, 10):
            print(".", end="")
        print("]")
        if number != 10:
            print("Still loading...")



number = int(input())
loading_bar(number)