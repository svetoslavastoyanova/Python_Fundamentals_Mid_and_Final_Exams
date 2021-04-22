numbers = list(map(int, input().split(" ")))
total_sum = sum(numbers)
average = total_sum//len(numbers)
top_five = []
sorted_nums = []
counter = 0

for number in numbers:
    if len(numbers) < 5:
        print("No")

    elif number > average:
        top_five.append(number)
        top_five.sort(reverse=True)
        sorted_nums = top_five[:5]

print(" ".join(str(sorted_nums)))







