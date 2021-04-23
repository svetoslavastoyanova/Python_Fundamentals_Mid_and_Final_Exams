list = input().split("|")
budget = float(input())
profit = 0.0
bought_items = []
for items in list:
    element = items.split("->")
    item = element[0]
    price = float(element[1])

    if (budget - price) >= 0:
        if item == "Clothes" and price <= 50.00 or item == "Shoes" and price <= 35.00 or item == "Accessories" and price <= 20.50:
            budget -= price
            current_profit = price * 0.40
            profit += current_profit
            final_price = current_profit + price
            bought_items.append(final_price)
result = []
for item in bought_items:
    item = f"{item:.2f}"
    result.append(item)

print(" ".join(result))
print(f"Profit: {profit:.2f}")
final_counts = budget + sum(bought_items)
if final_counts <= 150:
    print("Time to go.")
else:
    print(f"Hello, France!")





