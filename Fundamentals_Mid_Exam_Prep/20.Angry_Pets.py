price_ratings = list(map(int, input().split(" ")))
entry_point = int(input())
value = price_ratings[entry_point]
left_part = price_ratings[:entry_point]
right_part = price_ratings[entry_point:]
sum = []
for i in range(price_ratings + 1):
    type_of_items = input()
    type_of_price_ratings = input()

    if type_of_items == "cheap":
        if i < entry_point:
            sum.append(i)
        elif i >= entry_point:
            sum.append(i)


