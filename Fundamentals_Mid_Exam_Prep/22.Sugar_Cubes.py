sugar_cubes = list(map(int, input().split(" ")))
line = input()

while line != "Mort":
    commands = line.split(" ")
    value = int(commands[1])

    if commands[0] == "Add":
        sugar_cubes.append(value)

    elif commands[0] == "Remove":
        if value in sugar_cubes:
            sugar_cubes.remove(value)

    elif commands[0] == "Replace":
        replacement = commands[2]
        if value in sugar_cubes:
            index = sugar_cubes.index(value)
            sugar_cubes.insert(index, replacement)
            sugar_cubes.pop(value)

    elif commands[0] == "Collapse":
        sugar_cubes = [n for n in sugar_cubes if n >= value]

    line = input()
print(" ".join(map(str, sugar_cubes)))