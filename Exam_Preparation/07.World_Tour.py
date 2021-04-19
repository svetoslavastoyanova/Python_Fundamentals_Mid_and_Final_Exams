line = input()

while True:
    data = input()
    if data == "Travel":
        break
    tokens = data.split(":")
    command = tokens[0]
    if command == "Add Stop":
        index = int(tokens[1])
        string = tokens[2]
        if index in range(len(line)):
            start_line = line[:index]
            end_line = line[index:]
            line = start_line+string+end_line

    elif command == "Remove Stop":
        start_index = int(tokens[1])
        end_index = int(tokens[2])
        if start_index in range(len(line)) and end_index in range(len(line)):
            start_line = line[:start_index]
            end_line = line[end_index+1:]
            line = start_line + end_line

    elif command == "Switch":
        old_string = tokens[1]
        new_string = tokens[2]
        if old_string in line:
            line = line.replace(old_string, new_string)

    print(line)
print(f"Ready for world tour! Planned stops: {line}")


