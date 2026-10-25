#Hospital Billing
print("HOSPITAL BILLING")

patient = input("Enter patient name: ")
consultation = float(input("Consultation charge: "))
diagnosis = float(input("Diagnostic charge: "))
treatment = float(input("Treatment charge: "))

total = consultation + diagnosis + treatment

if total < 0:
    print("Invalid charges")
else:
    if total >= 5000:
        concession = total * 0.10
    else:
        concession = 0

    final_bill = total - concession

    print("Patient:", patient)
    print("Total charges: Rs.", total)
    print("Concession: Rs.", concession)
    print("Final bill: Rs.", final_bill)

    if final_bill >= 5000:
        print("Classification: High bill")
    else:
        print("Classification: Regular bill")