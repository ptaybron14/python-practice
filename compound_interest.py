# Compound interest calculator

print("Compound Interest Calculator")

# Get user input
principal = float(input("Enter the principal: "))
interest = float(input("Enter the estimated interest rate in decimal form: "))
compound_years = int(input("Enter amount of compound years: "))

# Calculate future value
final_amount = principal * (1 + interest) ** compound_years

# Display result
print("Final amount: $" + str(round(final_amount, 2)))
