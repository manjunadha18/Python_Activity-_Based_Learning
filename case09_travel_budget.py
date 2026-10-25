#Travel Budget Analysis
print("TRAVEL BUDGET ANALYSIS")

budget = float(input("Enter travel budget in Rs.: "))

categories = ["Hotel", "Food", "Transport"]
expenses = []

for category in categories:
    amount = float(input("Enter " + category + " cost in foreign currency: "))
    rate = float(input("Enter INR exchange rate for " + category + ": "))
    expenses.append(amount * rate)

total = sum(expenses)
fee = total * 0.02
final_cost = total + fee

print("\nTRAVEL EXPENSE SUMMARY")

for i in range(len(categories)):
    print(categories[i], ": Rs.", round(expenses[i], 2))

print("Conversion fee (2%): Rs.", round(fee, 2))
print("Total travel cost: Rs.", round(final_cost, 2))
print("Budget: Rs.", budget)

if final_cost <= budget:
    print("Status: Within budget")
else:
    print("Status: Over budget")

largest = expenses.index(max(expenses))
print("Largest expense:", categories[largest])