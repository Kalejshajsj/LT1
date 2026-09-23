#import math library for math features
import math

#inputs data from user for calculation
radius = float(input('Enter radius in meters: '))

#calculates area here
area = math.pi * (radius ** 2)
circumference = 2 * math.pi * radius
root = math.sqrt(area)
round_up = math.floor(area)
round_down = math.ceil(area)

#displays area  with area, circumference, and square root rounded up to 2 decimal places
print(f"Area of the Garden: {area:.2f} square meters")
print(f"Circumference of the Garden: {circumference:.2f} meters")
print(F"Square root of the area: {root:.2f}")
print(f"Area rounded up: {round_up}")
print(f"Area rounded down: {round_down}")



