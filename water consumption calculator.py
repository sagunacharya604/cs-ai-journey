print("WATER CONSUMPTION CALCULATOR")

family_members = int(input("Enter number of family members: "))

water_per_person = float(input("Enter daily water usage per person (in liters): "))

daily_usage = family_members * water_per_person

monthly_usage = daily_usage * 30

print("Total daily water usage =", daily_usage, "liters")

print("Total monthly water usage =", monthly_usage, "liters")

if daily_usage > 500:
    print("Warning: High water consumption")
else:
    print("Water usage is normal")
