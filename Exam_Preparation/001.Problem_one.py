import re

regex = r"([U$]{2}([A-Z][a-z]{2,})[U$]{2}[P@$]{3}([a-zA-Z]{5,}\d+)[P@$]{3})"
n = int(input())
count = 0
for i in range(n):
    line = input()
    is_matches = re.findall(regex, line)
    if is_matches:
        count += 1
        print(f"Registration was successful")
        for m in is_matches:
            print(f"Username: {m[1]}, Password: {m[2]}")
    else:
        print(f"Invalid username or password")

print(f"Successful registrations: {count}")


