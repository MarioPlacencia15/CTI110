# Mario Placencia
# 02/27/2025
# P1HW2
# This project shows the code for a budget

print("This program calculates and displays travel expenses")

# Input as integers
budget = int(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas_cost = int(input("How much do you think you will spend on gas? "))
accommodation_cost = int(input("Approximately, how much will you need for accommodation/hotel? "))
food_cost = int(input("Last, how much do you need for food? "))

 # Calculations with integers
total_expenses = gas_cost + accommodation_cost + food_cost
remaining_balance = budget - total_expenses

# Display results
print("\n--------------------Travel Expenses--------------------")
print(f"Location: {destination}")
print(f"Initial Budget: {budget}")
print(f"\nFuel: {gas_cost}")
print(f"Accommodation: {accommodation_cost}")
print(f"Food: {food_cost}")
print(f"\nRemaining Balance: {remaining_balance}")
