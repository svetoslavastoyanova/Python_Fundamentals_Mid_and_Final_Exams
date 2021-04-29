list = list(map(int, input().split(" ")))

line = input()
while line != "end":
    tokens = line.split(" ")
    command = tokens[0]
    if command == "swap":
        index_one = int(tokens[1])
        index_two = int(tokens[2])
        list[index_one], list[index_two] = list[index_two], list[index_one]
    elif command == "multiply":
        index_one = int(tokens[1])
        index_two = int(tokens[2])
        new_index = list[index_one]*list[index_two]
        list[index_one] = new_index
    elif command == "decrease":
        for index in range(len(list)):
            list[index] -= 1

    line = input()
print(', '.join(map(str, list)))