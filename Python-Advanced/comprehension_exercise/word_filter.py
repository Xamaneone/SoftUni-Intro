def is_even_lenght(word):
    if len(word) % 2 == 0:
        return True
    return False

def print_result(result):
    [print(word) for word in result]



strings = input().split(" ")
filtered_words = [word for word in strings if is_even_lenght(word)]
print_result(filtered_words)