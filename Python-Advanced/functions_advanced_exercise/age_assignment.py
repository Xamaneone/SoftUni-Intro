def age_assignment(*args, **kwargs):
    result_dict = {}
    for name in args:
        for letter in kwargs.keys():
            if name.startswith(letter):
                result_dict[name] = kwargs.get(letter)
    return result_dict


# print(age_assignment("Peter", "George", G=26, P=19))
# print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))