line = input()
collection = {}
while line != "Results":
    tokens = line.split(":")
    command = tokens[0]
    if command == "Add":
        person_name = tokens[1]
        health = int(tokens[2])
        energy = int(tokens[3])
        if person_name not in collection:
            collection[person_name] = {"h": health, "e": energy}
        else:
            collection[person_name]["h"] += health

    elif command == "Attack":
        attacker_name = tokens[1]
        defender_name = tokens[2]
        damage = int(tokens[3])

        if attacker_name and defender_name in collection:
            if collection[defender_name]["h"] - damage <= 0:
                collection[attacker_name]["e"] -= 1
                print(f"{defender_name} was disqualified!")
                del collection[defender_name]
                if collection[attacker_name]["e"] <= 0:
                    print(f"{attacker_name} was disqualified!")
                    del collection[attacker_name]
            else:
                collection[defender_name]["h"] -= damage
                collection[attacker_name]["e"] -= 1
                if collection[attacker_name]["e"] <= 0:
                    print(f"{attacker_name} was disqualified!")
                    del collection[attacker_name]

    elif command == "Delete":
        username = tokens[1]
        if username == "ALL":
            collection.clear()
        else:
            if username in collection:
                del collection[username]
    line = input()

people_count = len(collection.keys())
print(f"People count: {people_count}")
for key, value in sorted(collection.items(), key=lambda x: (-x[1]['h'], x[1]['e'], x[0])):
    print(f"{key} - {value['h']} - {value['e']}")