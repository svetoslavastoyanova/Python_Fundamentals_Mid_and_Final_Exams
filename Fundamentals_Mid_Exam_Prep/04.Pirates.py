command = input().split("||")

while command != "End":
    town = command[0]
    population = int(command[1])
    gold = int(command[2])

    if command == "Sail":
        command = input().split("=>")
        events = command[0]
        towns = command[1]
        people = command[2]
        treasure = command[3]

    command = input()






