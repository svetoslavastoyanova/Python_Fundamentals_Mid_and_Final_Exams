targets_sequence = list(map(int, input().split(" ")))
line = input()
while line != "End":
    tokens = line.split(" ")
    command = tokens[0]

    if command == "Shoot":
        index = int(tokens[1])
        value = int(tokens[2])
        if index in range(len(targets_sequence)):
            targets_sequence[index] -= value
            if targets_sequence[index] <= 0:
                targets_sequence.pop(index)

    elif command == "Add":
        index = int(tokens[1])
        value = int(tokens[2])

        if index in range(len(targets_sequence)):
            targets_sequence.insert(index, value)
        else:
            print("Invalid placement!")

    elif command == "Strike":
        index = int(tokens[1])
        radius = int(tokens[2])
        start = index - radius
        end = index + radius
        if start in range(len(targets_sequence)) and end in range(len(targets_sequence)):
            del targets_sequence[start: end + 1]
        else:
            print("Strike missed!")

    line = input()
print('|'.join(map(str, targets_sequence)))