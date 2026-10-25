#Retail Billing and Discounts
print("RETAIL BILLING")

quantity = int(input("Enter quantity: "))
price = float(input("Enter price per item: "))

if quantity < 0 or price < 0:
    print("Invalid input")
else:
    subtotal = quantity * price

    if subtotal >= 5000:
        discount = subtotal * 0.15
    elif subtotal >= 2000:
        discount = subtotal * 0.10
    else:
        discount = subtotal * 0.05

    discounted_amount = subtotal - discount
    tax = discounted_amount * 0.05
    total = discounted_amount + tax

    print("Subtotal: Rs.", subtotal)
    print("Discount: Rs.", discount)
    print("Tax (5%): Rs.", tax)
    print("Final bill: Rs.", total)