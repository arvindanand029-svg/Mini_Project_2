print("========== SMART CANTEEN ==========")


items = [
    ("Veg Sandwich", 60),
    ("Masala Dosa", 80),
    ("Chole Rice", 90),
    ("Paneer Roll", 100),
    ("Tea", 20)
]


for i in range(len(items)):
    print(f"{i + 1}. {items[i][0]} - ₹{items[i][1]}")


orders = []
subtotal = 0


while True:
    try:
        choice = int(input("\nChoose item number (1-5): "))

        if choice < 1 or choice > 5:
            print("Invalid item number! Please choose 1-5.")
            continue

        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be a positive integer!")
            continue


        name, price = items[choice - 1]
        cost = price * quantity

        orders.append((name, quantity, cost))
        subtotal += cost

        print(f"Added: {name} x {quantity} = ₹{cost:.2f}")

    except ValueError:
        print("Invalid input! Please enter a whole number.")
        continue

    again = input("Add another item? (y/n): ").lower()

    if again == "n":
        break
    elif again != "y":
        print("Invalid choice. Finishing the order.")
        break

if len(orders) == 0:
    print("\nNo order was placed.")
else:
    if subtotal >= 500:
        discount = subtotal * 0.10
    elif subtotal >= 250:
        discount = subtotal * 0.05
    else:
        discount = 0

    final_total = subtotal - discount

    print("\n========== RECEIPT ==========")

    for name, quantity, cost in orders:
        print(f"{name} x {quantity}: ₹{cost:.2f}")

    print("-----------------------------")
    print(f"Subtotal:     ₹{subtotal:.2f}")
    print(f"Discount:     ₹{discount:.2f}")
    print(f"Final total:  ₹{final_total:.2f}")
    print("=============================")
    print("Thank you for visiting!")
