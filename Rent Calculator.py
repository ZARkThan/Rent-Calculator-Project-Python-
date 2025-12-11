## Inputs we need from the user
rent = int(input("Enter your hostel/flat rent = "))# Total rent
food = int(input("Enter the amount of food ordered = "))# Total food ordered for snacking
electricity_spend = int(input("Enter the total of electricity spend = "))# Electricity units spend
charge_per_unit = int(input("Enter the charge per unit = ")) #Charge per unit
persons = int(input("Enter the number of persons living in room/flat = "))# Persons living in room/flat

total_bill = electricity_spend * charge_per_unit

output = (food + rent + total_bill) // persons ## Output

print("Each person will pay = ", output)  # Total amount you've to pay is

