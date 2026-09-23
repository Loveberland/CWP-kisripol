#include stdio.h
def highlow(word):
    swapped_word = ""
    for i in word:
        if i.islower():
            swapped_word += i.upper()
        else:
            swapped_word += i.lower()
    return swapped_word

if __name__ == "__main__":
    print(highlow(input()))
