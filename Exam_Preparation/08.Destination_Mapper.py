import re


regex = r"([=|/])([A-Z][a-zA-Z]{2,})\1"
line = input()
list = []

matches = re.finditer(regex, line)
for m in matches:
    list.append(m[2])
print(f"Destinations: {', '.join(list)}")
print(f"Travel Points: {len(''.join(list))}")


