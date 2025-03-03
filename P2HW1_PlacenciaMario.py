# Mario Placencia
# 03/02/2025
# P2HW1
# This project shows the code for a budget better formatted 

print("This program calculates and displays travel expenses")

# Input as floats
budget = float(input("\nEnter Budget: "))
destination = input("\nEnter your travel destination: ")
gas_cost = float(input("\nHow much do you think you will spend on gas? "))
accommodation_cost = float(input("\nApproximately, how much will you need for accommodation/hotel? "))
food_cost = float(input("\nLast, how much do you need for food? "))

 # Calculations
total_expenses = gas_cost + accommodation_cost + food_cost
remaining_balance = budget - total_expenses

# Display results
print("\n----------Travel Expenses----------")
print(f"Location:           {destination}")
print(f"Initial Budget:     ${budget:.2f}")
print(f"Fuel:               ${gas_cost:.2f}")
print(f"Accommodation:      ${accommodation_cost:.2f}")
print(f"Food:               ${food_cost:.2f}")
print("-------------------------------------")
print(f"\nRemaining Balance:  ${remaining_balance:.2f}")

