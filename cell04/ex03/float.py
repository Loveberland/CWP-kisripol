import math

number_input = input("Give me a number: ")
numeric_value = float(number_input)
if math.floor(numeric_value) != numeric_value:
    print("This number is an dicimal.")
else:
    print("This number is an integer")
