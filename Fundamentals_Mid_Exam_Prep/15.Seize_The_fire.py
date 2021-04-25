type_of_fire = input().split("#")
amount_of_water = int(input())
effort = 0
total_fire = 0
list_of_numbers = []

print(f"Cells:")

for types in type_of_fire:
    command = types.split(" = ")
    type = command[0]
    number = int(command[1])

    if amount_of_water < number:
        continue
    if type == "High" and 81 <= number <= 125:
        amount_of_water -= number
        total_fire += number
        effort += number*0.25
        list_of_numbers.append(number)

    elif type == "Medium" and 51 <= number <= 80:
        amount_of_water -= number
        total_fire += number
        effort += number * 0.25
        list_of_numbers.append(number)

    elif type == "Low" and 1 <= number <= 50:
        amount_of_water -= number
        total_fire += number
        effort += number * 0.25
        list_of_numbers.append(number)

for cells in list_of_numbers:
    print(f"- {cells}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")




