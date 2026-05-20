print("MOTION CALCULATOR")

speed = float(input("Enter speed in m/s: "))

time = float(input("Enter time in seconds: "))

distance = speed * time

print("Distance travelled =", distance, "meters")

if distance > 1000:
    print("Long distance travelled")
else:
    print("Short distance travelled")
