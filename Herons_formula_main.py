
#Area of triangle by Heron's Formula

import math
import sys

#User Input for the sides value

#a1

a1 = input("->Enter the length of a(cm): ")

if a1.replace(".","").isdigit():
    a1 = float(a1)
    print("Done")
else:
    print("INVALID CHARACTERS")
    sys.exit()

#b1

b1 = input("->Enter the length of b(cm): ")

if b1.replace(".","").isdigit():
    b1 = float(b1)
    print("Done")
else:
    print("INVALID CHARACTERS")
    sys.exit()
#c1

c1 = input("->Enter the length of c(cm): ")

if c1.replace(".","").isdigit():
    c1 = float(c1)
    print("Done")
else:
    print("INVALID CHARACTERS")
    sys.exit()
#Finding Semi-Perimeter(s)

s = (a1 + b1 + c1)/2

#Checking if its an valid triangle

if (a1 + b1 > c1) and (b1 + c1 > a1) and (c1 + a1 > b1):
    #Area
    Area = math.sqrt(s * (s - a1) * (s - b1) * (s - c1))
    Area = round(Area, 2)
    #Result
    print(f"->Area of your tringle: {Area} cm^2")
else:
    print("Its not a valid triangle")
    sys.exit()

