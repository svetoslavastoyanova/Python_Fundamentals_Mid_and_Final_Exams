list_of_nums = list(map(int, input().split(" ")))
line = input()

while line != "END":
    command = line.split(" ")
    to_do = command[0]

    if to_do == "Change":
        first_num = int(command[1])
        second_num = int(command[2])
        if first_num in list_of_nums:
            index_first = list_of_nums.index(first_num)
            list_of_nums.insert(index_first, second_num)
            list_of_nums.remove(first_num)

    if to_do == "Hide":
        first_num = int(command[1])
        if first_num in list_of_nums:
            list_of_nums.remove(first_num)

    if to_do == "Switch":
        first_num = int(command[1])
        second_num = int(command[2])
        if first_num and second_num in list_of_nums:
            index_first = list_of_nums.index(first_num)
            index_second = list_of_nums.index(second_num)
            list_of_nums[index_first], list_of_nums[index_second] = list_of_nums[index_second], list_of_nums[index_first]

    if to_do == "Insert":
        index = int(command[1])
        number = int(command[2])
        if index < len(list_of_nums):
            list_of_nums.insert(index + 1, number)

        if to_do == "Reverse":
            list_of_nums.reverse()

        line = input()
print(" ".join(map(str, list_of_nums)))



