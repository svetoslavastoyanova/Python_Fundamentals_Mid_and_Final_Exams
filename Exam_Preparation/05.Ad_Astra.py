import re
line = input()
regex = r"([#|\|])([a-zA-Z ]+)\1(\d{2}/\d{2}/\d{2})\1(\d+)\1"
total_calories = 0
max_calories = 2000
matches = re.finditer(regex, line)

for match in matches:
    total_calories += int(match[4])
needed_calories = (total_calories//max_calories)

print(f"You have food to last you for: {needed_calories} days!")
for match in re.findall(regex, line):
    item = match[1]
    date = match[2]
    calories = match[3]
    print(f"Item: {item}, Best before: {date}, Nutrition: {calories}")
