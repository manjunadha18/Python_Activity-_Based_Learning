#Employee Payroll
print("EMPLOYEE PAYROLL")

name = input("Enter employee name: ")
basic = float(input("Enter basic salary: "))
allowance = float(input("Enter allowances: "))
overtime = float(input("Enter overtime payment: "))
incentive = float(input("Enter incentives: "))

gross = basic + allowance + overtime + incentive

if min(basic, allowance, overtime, incentive) < 0:
    print("Invalid salary details")
else:
    if gross <= 20000:
        deduction = gross * 0.05
    elif gross <= 40000:
        deduction = gross * 0.10
    else:
        deduction = gross * 0.15

    net = gross - deduction

    print("Employee:", name)
    print("Gross salary: Rs.", gross)
    print("Deduction: Rs.", deduction)
    print("Net salary: Rs.", net)