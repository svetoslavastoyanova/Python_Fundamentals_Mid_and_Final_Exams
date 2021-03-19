strawberries = 3.50
blueberries = 5
row_counts = int(input())
position_counts = int(input())
price1 = 0
price2 = 0
counter1 = 0
counter2 = 0
discount = 0.8

for rows in range(1, row_counts + 1):
    if rows % 2 != 0:
        price1 += strawberries
    for position in range(1, position_counts + 1):

        if rows % 2 == 0 and position % 3 != 0:
            price2 += blueberries
            break





