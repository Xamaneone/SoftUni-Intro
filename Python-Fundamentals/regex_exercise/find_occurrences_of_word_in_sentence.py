import re

line = input()
keyword = input()

pattern = f"\\b{keyword}\\b"
result = re.findall(pattern, line, re.IGNORECASE)

print(len(result))