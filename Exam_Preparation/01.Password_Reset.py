line = input()
line_two = input()
while line_two != "Done":
    tokens = line_two.split(" ")
    command = tokens[0]
    if command == "TakeOdd":
        string = ""
        for i in range(len(line)):
            if i % 2 != 0:
                string += line[i]
        line = string
        print(line)

    elif command == "Cut":
        index = int(tokens[1])
        length = int(tokens[2])
        left_part = line[:index]
        right_part = line[index+length:]
        line = left_part + right_part
        print(line)

    elif command == "Substitute":
        substring = tokens[1]
        substitute = tokens[2]
        if substring in line:
            line = line.replace(substring, substitute)
            print(line)
        else:
            print(f"Nothing to replace!")

    line_two = input()
print(f"Your password is: {line}")