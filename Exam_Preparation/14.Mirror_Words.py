import re

regex = r"(#|@)([a-zA-Z]{3,})\1(#|@)([a-zA-Z]{3,})\1"
line = input()
pairs = []
total_match = 0
is_mirror = False
matches = re.findall(regex, line)
for m in matches:
    total_match += 1
    first_word = m[1]
    second_word = m[3]
    word_to_compare = second_word[::-1]
    if first_word == word_to_compare:
        pairs.append(first_word+" <=> "+second_word)
        is_mirror = True

if total_match == 0:
    print(f"No word pairs found!")
    print(f"No mirror words!")
else:
    print(f"{total_match} word pairs found!")
if total_match > 0:
    if is_mirror == False:
        print(f"No mirror words!")
    else:
        print(f"The mirror words are:")
        print(', '.join(pairs))




