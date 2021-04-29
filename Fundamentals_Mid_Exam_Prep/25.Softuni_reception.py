first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
student_count = int(input())
counter = 0
total_students_answered = 0
while total_students_answered <student_count:
    total_students_answered += first_employee+second_employee+third_employee
    counter += 1
    if counter % 4 == 0:
        counter += 1
        continue
print(f"Time needed: {counter}h.")