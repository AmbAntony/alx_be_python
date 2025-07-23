monthly_income = float(input("Enter your monthly income: "))
monthly_expense = float(input("Enter your monthly expense: "))

monthly_savings = monthly_income - monthly_expense
annual_savings = monthly_savings * 12

projected_savings = annual_savings + (annual_savings * 0.05)

print(f"Your monthly savings are {monthly_savings}")
print(f"Your total savings are {projected_savings}")