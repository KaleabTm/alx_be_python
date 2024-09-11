#define variable and accept user input
income = int(input("Enter your monthly income:"))
expenses = int(input("Enter your total monthly expenses:"))


#calculate monthly savings
monthly_Savings = income - expenses

#calculate annual savings
projected_Savings = monthly_Savings * 12 + (monthly_Savings * 12 * 0.05)

#print monthly savings and annual savings
print(f"Your monthly savings are ${monthly_Savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_Savings}.")

