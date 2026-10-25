#Campus Event Financial Planning
print("CAMPUS EVENT FINANCIAL PLANNING")

venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
catering = float(input("Enter catering cost per person: "))
transport = float(input("Enter transport cost: "))
certificates = float(input("Enter certificate cost per person: "))
sponsorship = float(input("Enter sponsorship amount: "))
fee = float(input("Enter registration fee per person: "))

fixed_cost = venue + equipment + transport
per_person_cost = catering + certificates
total_cost = fixed_cost + 100 * per_person_cost

if min(venue, equipment, catering, transport,
       certificates, sponsorship, fee) < 0:
    print("Invalid input")
else:
    shortfall = max(0, total_cost - sponsorship)
    remaining = total_cost - sponsorship
    participants_needed = 0

    if fee > per_person_cost:
        participants_needed = max(
            0, (remaining + fee - 1) // (fee - per_person_cost)
        )
    elif remaining > 0:
        participants_needed = -1

    print("Fixed cost: Rs.", fixed_cost)
    print("Total cost for 100 participants: Rs.", total_cost)
    print("Sponsorship: Rs.", sponsorship)
    print("Funding shortfall: Rs.", shortfall)

    if participants_needed == -1:
        print("Registration fee cannot cover the remaining cost.")
    else:
        print("Minimum participants to cover costs:",
              int(participants_needed))