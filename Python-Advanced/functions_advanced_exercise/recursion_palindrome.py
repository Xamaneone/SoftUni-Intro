def palindrome(word, number, reverse_word=""):
    if len(word) == number:
        if word == reverse_word:
            return f"{word} is a palindrome"
        return f"{word} is not a palindrome"
    reverse_word += word[-number - 1]
    return palindrome(word, number + 1, reverse_word)


# print(palindrome("abcba", 0))
# print(palindrome("peter", 0))