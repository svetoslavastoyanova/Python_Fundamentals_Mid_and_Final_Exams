days_of_the_trip = int(input())
budget = float(input())
people = int(input())
price_per_fuel_per_km = float(input())
food_per_day = float(input())
room_price_per_day = float(input())
total_food_expenses = food_per_day * people * days_of_the_trip
total_price_for_hotel = room_price_per_day * people * days_of_the_trip
consumed_fuel = 0
money = total_price_for_hotel + total_food_expenses
if people <= 10:
    money = total_food_expenses + (total_price_for_hotel*0.25)



for days in range(1, days_of_the_trip + 1):
    travelled_distance_per_day = float(input())

    if money > budget:
        print(f"Not enough money to continue the trip.")
        break

    if days % 3 == 0 or days % 5 == 0:
        money += money * 0.4
    current_fuel = travelled_distance_per_day*price_per_fuel_per_km
    money += current_fuel

    if days % 7 == 0:
        withdraw = money / people
        money -= withdraw


if money <= budget:
    print(f"You have reached the destination. You have {(budget - money):.2f}$ budget left.")
else:
    print(f"Not enough money to continue the trip. You need {(money - budget):.2f}$ more.")




