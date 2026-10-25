#Railway Fare Calculator
print("RAILWAY FARE CALCULATOR")

distance = float(input("Enter distance in km: "))
age = int(input("Enter passenger age: "))

if distance <= 0 or age < 0:
    print("Invalid input")
else:
    fare = distance * 2
    reservation_fee = 30
    concession = 0

    if age < 5:
        fare = 0
        reservation_fee = 0
    elif age >= 60:
        concession = fare * 0.40

    total = fare - concession + reservation_fee

    print("Distance:", distance, "km")
    print("Base fare: Rs.", fare)
    print("Concession: Rs.", concession)
    print("Reservation fee: Rs.", reservation_fee)
    print("Total fare: Rs.", total)