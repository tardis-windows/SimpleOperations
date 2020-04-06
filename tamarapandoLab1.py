# Lab 1
# Tamara Pando
# afternoon 1 section Csc 113

import math
# question A
print("Question A: \n")
seconds = (42 * 60) + 42
print("There are", seconds, "seconds in 42 minutes and 42 seconds\n")

# question B
print("Question B: \n")
radius_1 = 4; radius_2 = 6

volume_1 = (4/3)*(math.pi*(math.pow(radius_1, 3)))
volume_2 = (4/3)*(math.pi*(math.pow(radius_2, 3)))

print("The volume of the sphere with radius 4 is:", volume_1)
print("The volume fo the sphere with radius 6 is:", volume_2, "\n")

# question C
print("Question C: \n")
temp = -40;

fahr_to_cels = (temp - 32)*(5/9)
celc_to_fahr = (temp * (9/5)) + 32

print("The conversion from Fahrenheit to Celsius of -40 degrees is: ", fahr_to_cels)
print("The conversion from Celsius to Fahrenheit of -40 degrees is: ", celc_to_fahr, "\n")

# question D
print("Question D: \n")

a = int(input("Enter the value of a: "))
cube_volume = math.pow(a, 3)
prism_volume = a*(2*a)*(3*a)

times_fits = prism_volume/cube_volume

print("Cube fits : ", times_fits, " inside the prism")
