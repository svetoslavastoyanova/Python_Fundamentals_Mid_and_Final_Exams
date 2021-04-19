key = input()

line = input()
while line != "Generate":
    tokens = line.split(">>>")
    command = tokens[0]
    if command == "Contains":
        substring = tokens[1]
        if substring in key:
            print(f"{key} contains {substring}")
        else:
            print(f"Substring not found!")

    elif command == "Flip":
        command_two = tokens[1]
        start_index = int(tokens[2])
        end_index = int(tokens[3])
        if command_two == "Upper":
            new_key = key[start_index:end_index].upper()
            start = key[:start_index]
            end = key[end_index:]
            key = start + new_key + end

        elif command_two == "Lower":
            new_key = key[start_index:end_index].lower()
            start = key[:start_index]
            end = key[end_index:]
            key = start + new_key + end
        print(key)

    elif command == "Slice":
        start_index = int(tokens[1])
        end_index = int(tokens[2])
        new_key = key[start_index:end_index]
        start = key[:start_index]
        end = key[end_index:]
        key = start+end
        print(key)
    line = input()
print(f"Your activation key is: {key}")