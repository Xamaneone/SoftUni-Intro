def char_in_range(start, stop):
    for char in range(ord(start) + 1, ord(stop)):
        print(chr(char), end=" ")
char_in_range(input(), input())
