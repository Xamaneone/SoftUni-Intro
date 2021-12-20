from collections import deque


def stock_availability(items, act, *args):
    items = deque(items)
    if act == "delivery":
        for arg in args:
            items.append(arg)
        return list(items)
    elif act == "sell":
        if not args:
            items.popleft()
            return list(items)
        else:
            for arg in args:
                if str(arg).isdigit():
                    for n in range(arg):
                        items.popleft()
                    return list(items)
                else:
                    for arg in args:
                        while arg in items:
                            items.remove(arg)
                    return list(items)








#
# print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
# print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))


