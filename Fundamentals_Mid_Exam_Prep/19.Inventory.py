collecting_items = input().split(", ")
line = input()

while line != "Craft!":
    tokens = line.split(" - ")
    command = tokens[0]
    item = tokens[1]

    if command == "Collect":
        if not item in collecting_items:
            collecting_items.append(item)
    elif command == "Drop":
        if item in collecting_items:
            collecting_items.remove(item)
    elif command == "Combine Items":
        new_item = item.split(":")
        item_one = new_item[0]
        item_two = new_item[1]
        if item_one in collecting_items:
            index_one = collecting_items.index(item_one)
            collecting_items.insert(index_one + 1, item_two)
    elif command == "Renew":
        if item in collecting_items:
            collecting_items.remove(item)
            collecting_items.append(item)
    line = input()

print(", ".join(collecting_items))