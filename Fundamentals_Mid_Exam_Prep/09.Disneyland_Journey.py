journey_price = float(input())
months_needed = int(input())
spent_money = 0
for month in range(1, months_needed + 1):
    if month % 2 != 0 and month != 1:
        spent_money -= spent_money * 0.16

    elif month % 4 == 0:
        spent_money += spent_money*0.25

    spent_money += journey_price * 0.25

if spent_money >= journey_price:
    print(f"Bravo! You can go to Disneyland and you will have {(spent_money - journey_price):.2f}lv. for souvenirs.")
else:
    print(f"Sorry. You need {abs(journey_price - spent_money):.2f}lv. more.")