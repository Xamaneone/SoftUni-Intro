text = input()
emoticons = []
emoticon = False
for word in text:
    if emoticon is True:
        emoticon = False
        emoticons.append(f":{word}")
        if word == ":":
            emoticon = True
    elif word == ":":
        emoticon = True
print("\n".join(emoticons))