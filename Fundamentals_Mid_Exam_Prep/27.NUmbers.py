numbers = list(map(int, input().split(" ")))
average = sum(numbers)//len(numbers)
numbers = numbers[::-1]
greater_nums = []

for index in range(len(numbers)):
    if numbers[index] > average:
        greater_nums.append(numbers[index])
greater_nums = sorted(greater_nums, reverse=True)
if len(greater_nums) > 5:
    greater_nums = greater_nums[:5]
    print(' '.join(map(str, greater_nums)))
elif 0 < len(greater_nums) <= 5:
    print(' '.join(map(str, greater_nums)))
elif len(greater_nums) == 0:
    print("No")


