1. Loan Eligibility Checker

age = int(input("Enter Age: "))
salary = int(input("Enter Salary: "))
if age >= 21 and salary >= 25000:
    print("Eligible for Loan")
else:
    print("Not Eligible")


2. Voting Eligibility Verification

age = int(input("Enter Age: "))
if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible")


3. Employee Bonus Eligibility

years = int(input("Years of Service: "))
salary = int(input("Salary: "))
if years >= 5 and salary >= 30000:
    print("Bonus Eligible")
else:
    print("Not Eligible")


4. Admission Eligibility Check

marks = int(input("Enter Percentage: "))
if marks >= 60:
    print("Admission Granted")
else:
    print("Admission Denied")


5. Scholarship Eligibility Verification

marks = int(input("Enter Percentage: "))
income = int(input("Enter Family Income: "))
if marks >= 75 and income <= 200000:
    print("Scholarship Eligible")
else:
    print("Not Eligible")

