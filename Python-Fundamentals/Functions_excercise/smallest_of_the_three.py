def smallest(first_num, second_num, third_num):
    the_lower = first_num
    if first_num > second_num:
        the_lower = second_num
    if second_num > third_num:
        the_lower = third_num
    return the_lower
print(smallest(int(input()), int(input()), int(input())))