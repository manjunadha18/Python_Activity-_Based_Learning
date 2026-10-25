#University Scholarship Allocation
print("UNIVERSITY SCHOLARSHIP ALLOCATION")

name = input("Enter student name: ")
marks = float(input("Enter aggregate marks (%): "))
attendance = float(input("Enter attendance (%): "))
income = float(input("Enter annual family income: "))

if (marks >= 75 and attendance >= 75
        and income <= 250000):
    print("Student Name:", name)
    print("Status: Eligible for scholarship")
else:
    print("Student Name:", name)
    print("Status: Not eligible for scholarship")