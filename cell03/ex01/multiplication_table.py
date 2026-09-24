def multiplication_table(number):
    for multiplier in range(10):
        print(f"{multiplier} x {number} = {multiplier * number}")


if __name__ == "__main__":
    multiplication_table(int(input("Enter a number\n")))
