collection = input().split(" ")
command = input()

while command != "Stop":
    tokens = command.split(" ")
    to_do = tokens[0]

    if to_do == "Delete":
        index = int(tokens[1])+1
        if index >= 0 and index < len(collection):
            collection.pop(index)

    elif to_do == "Swap":
        word_one = tokens[1]
        word_two = tokens[2]
        if word_one and word_two in collection:
            index_first = collection.index(word_one)
            index_second = collection.index(word_two)
            collection[index_first], collection[index_second] = collection[index_second], collection[index_first]

    elif to_do == "Put":
        word_one = tokens[1]
        index = int(tokens[2])-1
        if index >= 0 and index < (len(collection)+1):
            collection.insert(index, word_one)


    elif to_do == "Sort":
        collection.sort(reverse=True)

    elif to_do == "Replace":
        word_one = tokens[1]
        word_two = tokens[2]
        if word_two in collection:
            index_second = collection.index(word_two)
            collection.insert(index_second, word_one)
            collection.remove(word_two)

    command = input()
print(" ".join(collection))
