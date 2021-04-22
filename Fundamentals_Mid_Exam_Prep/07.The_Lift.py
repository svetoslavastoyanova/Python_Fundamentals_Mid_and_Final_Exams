people_waiting = int(input())
state_of_lift = [int(x) for x in input().split(" ")]
MAX = 4

for index in range(len(state_of_lift)):
    while not state_of_lift[index] == MAX:
        if people_waiting > 0:
            state_of_lift[index] += 1
            people_waiting -= 1
        else:
            break

all_seats = len(state_of_lift) * MAX
taken_seats = sum(state_of_lift)

if people_waiting == 0 and taken_seats < all_seats:
    print(f"The lift has empty spots!")
elif people_waiting > 0 and taken_seats == all_seats:
    print(f"There isn't enough space! {people_waiting} people in a queue!")
print(" ".join([str(x) for x in state_of_lift]))




