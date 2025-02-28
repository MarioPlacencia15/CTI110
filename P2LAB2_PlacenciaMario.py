#Mario Placencia
#03/04/2025
#P2LAB2
#Using dictionaries

cars = {'Camaro':18.21, 'Prius':52.36, 'Model S': 110, 'Silverado':26}

#Get keys from dict
cars_keys = cars.keys()
print(cars_keys)
print(*cars_keys, sep = ",")

#Get a car from user
car_name = input("enter a car: ")

#Get MPG for give car
car_mpg = cars[car_name]
print(f"The {car_name} gets {car_mpg} miles per gallon.")

#Get mils from user

miles_driven = float(input(f"How many miles will you drive the {car_name}?"))

#calculate

gallons_needed = miles_driven/car_mpg

#Display reults
print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {car_name} {miles_driven} miles")
