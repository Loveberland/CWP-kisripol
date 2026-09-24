import sys

guessed_parameter = input("What was the parameter? ")
if guessed_parameter == sys.argv[1]:
    print("Good job!")
else:
    print("Nope, sorry...")
