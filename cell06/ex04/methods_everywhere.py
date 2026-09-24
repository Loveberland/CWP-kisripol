import sys


def shrink(string):
    return string[:8]


def enlarge(string):
    return string + "Z" * (8 - len(string))


if __name__ == "__main__":
    arguments_list = sys.argv
    arguments_list.pop(0)
    for argument in arguments_list:
        if len(argument) > 8:
            print(shrink(argument))
        else:
            print(enlarge(argument))
