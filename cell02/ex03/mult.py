def isnegative(number):
    try:
        numeric_value = float(number)
    except ValueError:
        print("Oi!! Please enter number")
        return
    if numeric_value == 0:
        print("This number is both positive and negative.")
    elif numeric_value > 0:
        print("this number is positive.")
    else:
        print("This number is negative.")


def multiply_cal(first_number, last_number):
    try:
        first_integer = int(first_number)
        second_integer = int(last_number)
    except ValueError:
        print("Oi!! Please enter integer")
        return
    return first_integer * second_integer


if __name__ == "__main__":
    first_number = input("Enter the first number:\n")
    last_number = input("Enter the second number:\n")
    product = multiply_cal(first_number, last_number)
    print(f"{first_number} x {last_number} = {product}")
    isnegative(product)
