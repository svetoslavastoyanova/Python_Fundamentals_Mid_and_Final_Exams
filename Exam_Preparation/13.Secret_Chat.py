line = input()

data = input()
while data != "Reveal":
    tokens = data.split(":|:")
    command = tokens[0]
    if command == "InsertSpace":
        index = int(tokens[1])
        start = line[:index]
        end = line[index:]
        line = start + " " + end
        print(line)

    elif command == "Reverse":
        substring = tokens[1]
        if substring in line:
            line = line.replace(substring, "", 1)+substring[::-1]
            print(line)
        else:
            print(f"error")

    elif command == "ChangeAll":
        substring = tokens[1]
        replacement = tokens[2]
        line = line.replace(substring, replacement)
        print(line)
    data = input()

print(f"You have a new text message: {line}")