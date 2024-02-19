# Welcome message
print("Welcome to the Tip Calculator")

# Get user inputs
bill = float(input("What was the total bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

# Calculate bill with tip
bill_with_tip = bill + (bill * tip / 100)

# Calculate bill per person
bill_per_person = bill_with_tip / people

# Round the final amount to two decimal places
final_amount = round(bill_per_person, 2)

# Print the result
print(f"Each person should pay: {final_amount}")
