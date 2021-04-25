
count_of_students = int(input())
count_of_lectures = int(input())
initial_bonus = int(input())
max_bonus = []
max_attendances = []

for students in range(1, count_of_students + 1):
    attendances = int(input())
    max_attendances.append(attendances)
    formula = attendances/count_of_lectures * (5 + initial_bonus)
    max_bonus.append(formula)

final_bonus = max(max_bonus)
final_attendance = max(max_attendances)
print(f"Max Bonus: {round(final_bonus)}.")
print(f"The student has attended {final_attendance} lectures.")



