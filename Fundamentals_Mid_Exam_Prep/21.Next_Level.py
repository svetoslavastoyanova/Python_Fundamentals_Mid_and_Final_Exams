amount_of_experience = float(input())
count_of_battles = int(input())
counter = 1
gathered_experience = 0
for battle in range(1, count_of_battles+1):
    current_experience = float(input())
    if battle % 3 == 0:
        gathered_experience += 0.15*current_experience + current_experience
    elif battle % 5 == 0:
        gathered_experience += (current_experience - (0.10*current_experience))
    elif battle % 15 == 0:
        gathered_experience += current_experience + 0.05*current_experience
    else:
        gathered_experience += current_experience

    if gathered_experience >= amount_of_experience:
        break
    counter += 1

if gathered_experience >= amount_of_experience:
    print(f"Player successfully collected his needed experience for {counter} battles.")
else:
    result = amount_of_experience - gathered_experience
    print(f"Player was not able to collect the needed experience, {result:.2f} more needed.")

