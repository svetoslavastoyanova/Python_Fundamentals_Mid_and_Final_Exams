elements = input().split()
line = input()
moves_counter = 0
while line != "end":
    tokens = line.split()
    first_index = int(tokens[0])
    second_index = int(tokens[1])
    moves_counter += 1
    if first_index == second_index or first_index < 0 or second_index < 0 or first_index >= len(elements) or second_index >= len(elements):
        elements.insert(int(len(elements) / 2), f"-{str(moves_counter)}a")
        elements.insert(int(len(elements) / 2), f"-{str(moves_counter)}a")
        print(f"Invalid input! Adding additional elements to the board")
    elif elements[first_index] == elements[second_index]:
        print(f"Congrats! You have found matching elements - {elements[first_index]}!")
        x = elements.pop(first_index)
        elements.remove(x)
    elif elements[first_index] != elements[second_index]:
        print(f"Try again!")

    if len(elements) == 0:
        print(f"You have won in {moves_counter} turns!")
        break

    line = input()
if line == "end":
    print("Sorry you lose :(\n"
    f"{' '.join(elements)}")