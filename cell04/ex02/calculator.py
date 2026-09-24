def common_calculation(first_number, second_number):
    print(f"{first_number} + {second_number} = {first_number + second_number}")
    print(f"{first_number} - {second_number} = {first_number - second_number}")
    quotient = first_number / second_number
    print(f"{first_number} / {second_number} = %d" % quotient)
    print(f"{first_number} * {second_number} = {first_number * second_number}")


if __name__ == "__main__":
    first_number = int(input("Give me the first number: "))
    second_number = int(input("Give me the second number: "))
    print("Thank you!")
    common_calculation(first_number, second_number)
