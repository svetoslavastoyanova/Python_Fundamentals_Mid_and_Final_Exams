number_of_pieces = int(input())
collection = {}
for i in range(number_of_pieces):
    line = input()
    tokens = line.split("|")
    piece = tokens[0]
    composer = tokens[1]
    key = tokens[2]
    collection[piece] = {"composer": composer, "key": key}

line = input()
while line != "Stop":
    tokens = line.split("|")
    command = tokens[0]
    if command == "Add":
        piece = tokens[1]
        composer = tokens[2]
        key = tokens[3]
        if piece in collection:
            print(f"{piece} is already in the collection!")
        else:
            collection[piece] = {"composer": composer, "key": key}
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif command == "Remove":
        piece = tokens[1]
        if piece in collection:
            del collection[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif command == "ChangeKey":
        piece = tokens[1]
        new_key = tokens[2]
        if piece in collection:
            collection[piece]["key"] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    line = input()

sorted_collection = sorted(collection.items(), key=lambda x: (x[0], x[1]["composer"]))
for key, value in sorted_collection:
    print(f"{key} -> Composer: {value['composer']}, Key: {value['key']}")

