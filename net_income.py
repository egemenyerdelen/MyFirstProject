earned_amount = 202 + 118 + 2250 + 1680 + 1075 + 80
print("""Earned Amount: 
Bubblegum: $202
Toffee: $118 
Ice cream: $2250 
Milk chocolate: $1680 
Doughnut: $1075
Pancake: $80
""")
print(f"Income: ${earned_amount}")

staff_expenses = int(input("Staff expenses:"))
other_expenses = int(input("Other expenses:"))

net_income = earned_amount - (staff_expenses + other_expenses)

print(f"Net Income: ${net_income}")