n = int(input())
collection = {}
for _ in range(n):
    line = input().split("<->")
    plant = line[0]
    rarity = line[1]

    if plant not in collection:
        collection[plant] = {"Rarity": rarity, "Rating": []}
    else:
        collection[plant]["Rarity"] = rarity

data = input()
while data != "Exhibition":
    tokens = data.split(": ")
    command = tokens[1].split(" - ")
    command_type = tokens[0]
    plant = command[0]

    if plant not in collection:
        print(f"error")

    if command_type == "Rate":
        rating = command[1]
        collection[plant]["Rating"].append(int(rating))

    elif command_type == "Update":
        new_rarity = command[1]
        collection[plant]["Rarity"] = new_rarity

    elif command_type == "Reset":
        collection[plant]["Rating"].clear()
        collection[plant["Rating"] = 0.00

    data = input()
sorted_collection = sorted(collection.items(), key=lambda x: (x[1]['Rarity'], x[1]['Rating']), reverse=True)

for key, value in sorted_collection:
    print(f"{key}; Rarity: {value['Rarity']}; Rating: {sum(value['Rating'])/len(value['Rating']):.2f}")