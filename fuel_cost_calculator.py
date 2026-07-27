kilometers = float(input("How many kilometers do you want to drive? "))
petrol_price = float(input("Enter the current petrol price per liter (e.g. 22.45): "))
liters_needed = kilometers / 10
total_cost = liters_needed * petrol_price
total_cost = round(total_cost, 2)
liters_needed = round(liters_needed, 2)
print("----- FUEL COST CALCULATOR -----")
print(f"Distance: {kilometers} km")
print(f"Petrol price: R{petrol_price} per liter")
print(f"Liters needed: {liters_needed} L")
print(f"Total fuel cost: R{total_cost}")
print("---------------------------------")
