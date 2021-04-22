status_of_pirate_ship = list(map(int, input().split(">")))
warship = list(map(int, input().split(">")))
maximum_health = int(input())
status_count = 0
position = 0
is_sink = False
line = input()
while line != "Retire":
    tokens = line.split(" ")
    command = tokens[0]

    if command == "Fire":
        first_num = int(tokens[1])
        second_num = int(tokens[2])
        position = 0
        if first_num > 0 and first_num <= len(warship):
            position = first_num
            if warship[position] > 0:
                warship[position] -= second_num
            else:
                is_sink = True
                print(f"You won! The enemy ship has sunken.")
                break

    elif command == "Defend":
        first_num = int(tokens[1])
        second_num = int(tokens[2])
        damage = int(tokens[3])
        position = 0
        for i in range(first_num, second_num + 1):
            position = i
            if status_of_pirate_ship[position] >= second_num:
                status_of_pirate_ship[position] -= second_num
            else:
                print(f"You lost! The pirate ship has sunken.")
                is_sink = True
                break


    elif command == "Repair":
        first_num = int(tokens[1])
        second_num = int(tokens[2])
        position = 0
        if first_num <= 0 and first_num <= len(status_of_pirate_ship):
           if status_of_pirate_ship[position] + second_num <= maximum_health:
               diff = maximum_health - status_of_pirate_ship[position]
               status_of_pirate_ship[position] += diff
        else:
            status_of_pirate_ship[position] += second_num


    if command == "Status":
        status = maximum_health*0.2
        for index in status_of_pirate_ship:
            if index < status:
                status_count += 1
        print(f"{status_count} sections need repair.")

    line = input()
if True:
    print(f"Pirate ship status: {sum(status_of_pirate_ship)}")
    print(f"Warship status: {sum(warship)}")
