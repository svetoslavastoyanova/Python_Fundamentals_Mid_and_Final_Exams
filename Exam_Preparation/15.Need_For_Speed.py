number_of_cars = int(input())
collection = {}

for _ in range(number_of_cars):
    line = input()
    tokens = line.split("|")
    car = tokens[0]
    mileage = int(tokens[1])
    fuel = int(tokens[2])
    if car not in collection:
        collection[car] = {"mileage": 0, "fuel": 0}
        collection[car]["mileage"] = mileage
        collection[car]["fuel"] = fuel
data = input()

while data != "Stop":
    tokens = data.split(" : ")
    command = tokens[0]

    if command == "Drive":
        car = tokens[1]
        distance = int(tokens[2])
        fuel = int(tokens[3])
        if collection[car]["fuel"] < fuel:
            print(f"Not enough fuel to make that ride")
        else:
            collection[car]["mileage"] += distance
            collection[car]["fuel"] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if collection[car]["mileage"] >= 100000:
                print(f"Time to sell the {car}!")
                del collection[car]

    elif command == "Refuel":
        car = tokens[1]
        fuel = int(tokens[2])
        if fuel + collection[car]["fuel"] > 75:
            diff = 75 - collection[car]["fuel"]
            collection[car]["fuel"] += diff
            print(f"{car} refueled with {diff} liters")
        else:
            collection[car]["fuel"] += fuel
            print(f"{car} refueled with {fuel} liters")
    elif command == "Revert":
        car = tokens[1]
        kilometres = int(tokens[2])
        if collection[car]["mileage"] - kilometres < 10000:
            collection[car]["mileage"] = 10000
        else:
            collection[car]["mileage"] -= kilometres
            print(f"{car} mileage decreased by {kilometres} kilometers")

    data = input()
for key, value in sorted(collection.items(), key=lambda x: (-x[1]['mileage'], x[1]['fuel'], x[0])):
    print(f"{key} -> Mileage: {value['mileage']} kms, Fuel in the tank: {value['fuel']} lt.")