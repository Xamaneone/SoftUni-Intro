
type = input()

if type == "square":
    first = float(input())
    first = first * first
    first = (f"{first:.3f}")
    print (first)

elif type == "rectangle":
    first = float(input())
    second = float(input())
    result = first * second
    result = (f"{result:.3f}")
    print (result)

elif type == "circle":
    import math
    r = (float(input()))
    result = math.pi * r * r
    result = (f"{result:.3f}")
    print (result)

elif type == "triangle":
    first = float(input())
    second = float(input())
    result = first * second / 2
    result = (f"{result:.3f}")
    print (result)

