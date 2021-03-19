line = input()
top = 8848
counter = 1
meters = 5346

while line != "END":
    climbed_meters = int(input())
    if line == "Yes":
        counter += 1
        if counter > 5:
            break
    meters += climbed_meters
    line = input()
if meters >= top:
    print(f"Goal reached for {counter} days!")
else:
    print(f"Failed!")
    print(f"{meters}")
















