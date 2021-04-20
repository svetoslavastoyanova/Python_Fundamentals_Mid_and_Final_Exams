line = input()
collection = {}
while line != "Sail":
    tokens = line.split("||")
    town = tokens[0]
    population = int(tokens[1])
    gold = int(tokens[2])
    if town not in collection:
        collection[town] = {"Population": population, "Gold": gold }
    else:
        collection[town]['Population'] += population
        collection[town]["Gold"] += gold

    line = input()

data = input()
while data != "End":
    tokens = data.split("=>")
    command = tokens[0]
    town = tokens[1]

    if command == "Plunder" and town in collection:
        people = int(tokens[2])
        gold = int(tokens[3])
        collection[town]["Population"] -= people
        collection[town]["Gold"] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if collection[town]["Population"] <= 0 or collection[town]["Gold"] <= 0:
            del collection[town]
            print(f"{town} has been wiped off the map!")

    elif command == "Prosper":
        gold = int(tokens[2])
        if gold < 0:
            print(f"Gold added cannot be a negative number!")
        else:
            collection[town]["Gold"] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {collection[town]['Gold']} gold.")

    data = input()

if len(collection) > 0:
    print(f"Ahoy, Captain! There are {len(collection)} wealthy settlements to go to:")
    for key, value in sorted(collection.items(), key=lambda x: (-x[1]['Gold'], x[1]['Population'], x[0])):
        print(f"{key} -> Population: {value['Population']} citizens, Gold: {value['Gold']} kg")
else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")

