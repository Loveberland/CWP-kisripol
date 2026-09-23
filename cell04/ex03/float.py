import math
number_input = input("Give me a number: ")
if math.floor(float(number_input)) != float(number_input):
    print("This number is an dicimal.")
else:
    print("This number is an integer")
