#Mario Placencia
#03/02/2025
#P2HW2
#Showing results for grades in each module


# Get grades from the user
grade1 = float(input("Enter grade for Module 1: "))
grade2 = float(input("Enter grade for Module 2: "))
grade3 = float(input("Enter grade for Module 3: "))
grade4 = float(input("Enter grade for Module 4: "))
grade5 = float(input("Enter grade for Module 5: "))
grade6 = float(input("Enter grade for Module 6: "))

# Calculation
grades = [grade1, grade2, grade3, grade4, grade5, grade6]
lowest_grade = min(grades)
highest_grade = max(grades)
sum_of_grades = sum(grades)
average = sum_of_grades / len(grades)

# Display results
print("\n-----------------Results-----------------")
print(f"Lowest Grade:          {lowest_grade:.1f}")
print(f"Highest Grade:         {highest_grade:.1f}")
print(f"Sum of Grades:         {sum_of_grades:.1f}")
print(f"Average:               {average:.2f}")
print("-------------------------------------------------")
