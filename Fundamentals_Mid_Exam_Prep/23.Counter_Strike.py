energy = int(input())
line = input()
battle_counter = 0
while True:
    distance = int(line)
    if distance > energy:
        print(f"Not enough energy! Game ends with {battle_counter} won battles and {energy} energy")
        break
    else:
        energy -= distance
        battle_counter += 1
        if battle_counter % 3 == 0:
            energy += battle_counter
    line = input()
    if line == "End of battle":
        print(f"Won battles: {battle_counter}. Energy left: {energy}")
        break
