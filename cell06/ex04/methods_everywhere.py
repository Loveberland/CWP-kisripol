import sys
def shrink(string):
    return string[0:8]

def enlarge(string):
    return string+str("Z"*(8-len(string)))

if __name__ == "__main__":
    arguments_list = sys.argv
    arguments_list.pop(0)
    for i in arguments_list:
        if len(i) > 8:
            print(shrink(i))
        else:
            print(enlarge(i))
