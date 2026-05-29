print("PASCAL LAW PRESSURE CALCULATOR")

force = float(input("Enter force in Newtons: "))

area = float(input("Enter area in square meters: "))

pressure = force / area

print("Pressure =", pressure, "Pascals")

if pressure > 1000:
    print("High pressure generated")
else:
    print("Normal pressure generated")
