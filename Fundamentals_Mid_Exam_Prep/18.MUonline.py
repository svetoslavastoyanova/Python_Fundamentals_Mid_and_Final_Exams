dungeon_rooms = input().split("|")
bitcoins = 0
initial_health = 100
room = 0
final_room = len(dungeon_rooms)
is_dead = False
for rooms in dungeon_rooms:
    tokens = rooms.split(" ")
    command = tokens[0]
    number = int(tokens[1])
    room += 1
    if command == "potion":
        if (initial_health + number) > 100:
            current_health = 100
            diff = current_health - initial_health
            initial_health += diff
            print(f"You healed for {diff} hp.")
            print(f"Current health: {initial_health} hp.")
        else:
            initial_health += number
            print(f"You healed for {number} hp.")
            print(f"Current health: {initial_health} hp.")
    elif command == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")
    else:
        if (initial_health - number) > 0:
            initial_health -= number
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {room}")
            is_dead = True
            break
if not is_dead:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {initial_health}")










