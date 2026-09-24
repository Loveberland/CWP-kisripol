def password_check(word):
    expected_password = "Python is awesome"
    if word == expected_password:
        print("ACCESS GRANTED")
    else:
        print("ACCESS DENIED")


if __name__ == "__main__":
    password_check(input())
