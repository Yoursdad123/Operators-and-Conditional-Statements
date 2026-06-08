1. Simple Calculator

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)
print("Division =", a / b)
print("Modulus =", a % b)
print("Exponent =", a ** b)

2. Student Marks Calculation

m1 = int(input("Enter Marks 1: "))
m2 = int(input("Enter Marks 2: "))
m3 = int(input("Enter Marks 3: "))

total = m1 + m2 + m3
average = total / 3
percentage = total / 300 * 100

print("Total =", total)
print("Average =", average)
print("Percentage =", percentage)

3. Salary Calculation System

basic = float(input("Enter Basic Salary: "))

gross = basic + (0.20 * basic)
deduction = 0.10 * gross
net = gross - deduction

print("Gross Salary =", gross)
print("Deduction =", deduction)
print("Net Salary =", net)

4. Shopping Bill Calculator

price = float(input("Enter Product Price: "))
qty = int(input("Enter Quantity: "))
bill = price * qty
print("Total Bill =", bill)

5. Electricity Bill Calculation

units = int(input("Enter Units Consumed: "))
bill = units * 8
print("Electricity Bill =", bill)

