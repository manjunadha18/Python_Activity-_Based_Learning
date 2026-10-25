#Mobile Plan Cost Optimization
print("MOBILE PLAN COST OPTIMIZATION")

usage = float(input("Enter monthly data usage in GB: "))
budget = float(input("Enter your budget in Rs.: "))

# Plan details: name, monthly price, included data
plans = [
    ("Basic", 199, 10),
    ("Standard", 299, 25),
    ("Premium", 399, 50)
]

best_plan = None
best_cost = None

if usage < 0 or budget < 0:
    print("Invalid input")
else:
    for name, price, data in plans:
        extra = max(0, usage - data)
        total = price + extra * 10

        if total <= budget:
            if best_cost is None or total < best_cost:
                best_cost = total
                best_plan = name

    if best_plan is None:
        print("No plan fits your budget")
    else:
        print("Best plan:", best_plan)
        print("Total monthly cost: Rs.", best_cost)