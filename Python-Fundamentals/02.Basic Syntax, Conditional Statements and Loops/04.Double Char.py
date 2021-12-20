word = input()
mashup = ""
for i in range(0, len(word)):
    mashup += word[i] + word[i]
print(mashup)