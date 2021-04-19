import re


line = input()
numbers = {"key": 1}
emojis = {}
first_regex = r"(:{2}|\*{2})([A-Z][a-z]{2,})\1"
second_regex = r"(\d)"

second_match = re.findall(second_regex, line)
for second in second_match:
    numbers["key"] *= int(second)

first_match = re.finditer(first_regex, line)
for first in first_match:
    result = 0
    ascii = first[2]
    full_match = first[0]
    if full_match not in emojis:
        emojis[full_match] = {"key":0}

    for i in ascii:
        ch = ord(i)
        result += ch
    emojis[full_match]["key"] = result
print(f"Cool threshold: {numbers['key']}")
print(f"{len(emojis)} emojis found in the text. The cool ones are: ")
for key, value in emojis.items():
    if value['key'] >= numbers['key']:
        print(f"{key}")




