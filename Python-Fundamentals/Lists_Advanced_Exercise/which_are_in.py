keywords = input().split(", ")
strings = input().split(", ")
result = [subst for word in strings for subst in keywords if subst in word]
print(sorted(set(result), key=keywords.index))
