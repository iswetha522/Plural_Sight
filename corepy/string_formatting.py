print("The age of {0} is {1}".format('Jim', 32))
print("The age of {0} is {1}. {0}'s birthday is on {2}".format('Fred', 24, 'October 31'))
print("Reticulating spline {} of {}".format(4, 23))
print("Current position {latitude} {longitude}".format(latitude = "60N", longitude = "5E"))
print("Galactic position x = {pos[0]}, y = {pos[1]}, z = {pos[2]}".format(pos = (65.2, 23.1, 82.2)))
import math
print("Math constants: pi = {m.pi}, e = {m.e}".format(m = math))
print("Math constants: pi = {m.pi:.3f}, e = {m.e:.3f}".format(m = math))
value = 4 * 20
print("The value is {value}".format(value = value))

# Using f-strings
value = 4 * 20
print(f"The value is {value}")

import datetime
print(f"The current time is {datetime.datetime.now().isoformat()}.")

import math
print(f"Math constants: pi = {math.pi}, e = {math.e}")
print(f"Math constants: pi = {math.pi:.3f}, e = {math.e:.3f}")