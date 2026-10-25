#Manufacturing Cost and Profit
print("MANUFACTURING COST ANALYSIS")

quantity = int(input("Enter units produced: "))
material = float(input("Total material cost: "))
labour = float(input("Total labour cost: "))
machine = float(input("Total machine cost: "))
selling_price = float(input("Selling price per unit: "))

if (quantity <= 0 or min(material, labour, machine,
                          selling_price) < 0):
    print("Invalid input")
else:
    total_cost = material + labour + machine
    revenue = quantity * selling_price
    profit = revenue - total_cost
    profit_percent = profit / total_cost * 100 if total_cost > 0 else 0

    print("Total production cost: Rs.", total_cost)
    print("Total revenue: Rs.", revenue)
    print("Profit/Loss: Rs.", profit)
    print("Profit percentage:", round(profit_percent, 2), "%")

    if profit_percent >= 20:
        print("Target achieved")
    else:
        print("Target not achieved")