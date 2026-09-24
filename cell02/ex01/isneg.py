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


if __name__ == "__main__":
    isnegative(input())
