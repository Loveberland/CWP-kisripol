def from_this_to_that(current_number, target_number):
    while current_number != target_number:
        print(f"Inside the loop, my variable is {current_number}")
        if current_number < target_number:
            current_number += 1
        else:
            current_number -= 1


if __name__ == "__main__":
    starting_number = int(input("Enter a number less than 25\n"))
    if starting_number >= 25:
        print("Error")
    else:
        from_this_to_that(starting_number, 26)
