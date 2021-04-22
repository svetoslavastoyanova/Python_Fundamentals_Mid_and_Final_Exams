line = input()
total_without_tax = 0
taxes = 0
final_price = 0

while True:
    if line == "regular":
        taxes += total_without_tax * 0.2
        final_price = taxes + total_without_tax
        break

    elif line == "special":
        taxes += total_without_tax * 0.2
        final_price = taxes + total_without_tax
        final_price -= 0.10*final_price
        break


    prices = float(line)
    if prices < 0:
        print(f"Invalid price!")
    else:
        total_without_tax += prices
    if final_price == 0:
        print(f"Invalid order")

    line = input()

print(f"Congratulations you've just bought a new computer!")
print(f"Price without taxes: {total_without_tax:.2f}$")
print(f"Taxes: {taxes:.2f}$")
print(f"-----------")
print(f"Total price: {final_price:.2f}$")













