neighborhood = list(map(int, input().split("@")))

command = input()
position = 0

while not command == "Love!":
    length = int(command.split()[1])
    position += length
    if position >= len(neighborhood):
        position = 0

    if neighborhood[position] == 0:
        print(f"Place {position} already had Valentine's day.")
    else:
        neighborhood[position] -= 2
        if neighborhood[position] == 0:
            print(f"Place {position} has Valentine's day.")

    command = input()

print(f"Cupid's last position was {position}.")

success = len(neighborhood)
visited_places = [x for x in neighborhood if x == 0]
if success == visited_places:
    print(f"Mission successful")
else:
    print(f"Cupid has failed {len(visited_places)} places.")
