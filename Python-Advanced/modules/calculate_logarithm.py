from math import log

def calc_log(x, base):
    if base == "natural":
        return f"{log(x):.2f}"
    else:
        return f"{log(x, int(base)):.2f}"



print(calc_log(int(input()), str(input())))


