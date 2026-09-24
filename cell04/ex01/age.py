def whatmyage(age):
    for years_ahead in range(10, 31, 10):
        print(f"In {years_ahead} years, you'll be {age + years_ahead} years old.")


if __name__ == "__main__":
    whatmyage(int(input("Please tell me your age: ")))
