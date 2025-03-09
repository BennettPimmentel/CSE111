from datetime import date
import math

width = float(input("Enter the tire width in mm: "))
aspect_ratio = float(input("Enter the tire aspect ratio: "))
diameter = float(input("Enter the wheel diameter in inches: "))

volume = (math.pi * (width ** 2) * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000
volume = round(volume, 2)
current_date = date.today()

with open("volumes.txt", "a") as file:
    file.write(f"{current_date}, {int(width)}, {int(aspect_ratio)}, {int(diameter)}, {volume}\n")

print(f"The approximate tire volume is {volume} liters.")