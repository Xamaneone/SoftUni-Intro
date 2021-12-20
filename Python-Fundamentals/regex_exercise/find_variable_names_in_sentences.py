import re

line = input()
pattern = r"\b_(?P<variable>[0-9a-zA-Z]+)\b"

variables = re.findall(pattern, line)

print(','.join(variables))