line = input().split(" ")
data = input()
while data != "Stop":
    tokens = data.split(" ")
    command = tokens[0]
    if command == "Delete":
        index = int(tokens[1])
        if (index + 1) in range(len(line)):
            new_index = index+1
            line.pop(new_index)
    elif command == "Swap":
        word_one = tokens[1]
        word_two = tokens[2]
        if word_one in line and word_two in line:
            index_one = line.index(word_one)
            index_two = line.index(word_two)
            line[index_one],line[index_two] = line[index_two],line[index_one]
    elif command == "Put":
        word = tokens[1]
        index = int(tokens[2])
        new_index = index - 1
        end_index = line[-1]
        if new_index in range(len(line)):
            line.insert(new_index, word)
        elif new_index == end_index:
            line.append(word)

    elif command == "Sort":
        new_list = line.sort(reverse=True)

    elif command == "Replace":
        word_one = tokens[1]
        word_two = tokens[2]
        if word_two in line:
            index_two = line.index(word_two)
            line[index_two] = word_one
    data = input()
print(' '.join(line))

