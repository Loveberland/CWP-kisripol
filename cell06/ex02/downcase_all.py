import sys


def downcase_it(string):
    return string.lower()


if __name__ == "__main__":
    arguments_list = sys.argv
    arguments_list.pop(0)
    for argument in arguments_list:
        print(downcase_it(argument))
