#include stdio.h
'''Damn i accidently remove my cell03 folder and now im doing it again ;-;'''
def from_this_to_that(current_number, target_number):
    while current_number != target_number:
        print(f"Inside the loop, my variable is {current_number}")
        if current_number < target_number:
            current_number += 1
        else:
            current_number -= 1

if __name__ == "__main__":
    number = int(input("Enter a number less than 25\n"))
    if number >= 25:
        print("Error")
    else:
        from_this_to_that(number, 26)
