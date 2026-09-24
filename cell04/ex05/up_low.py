def highlow(word):
    swapped_word = ""
    for character in word:
        if character.islower():
            swapped_word += character.upper()
        else:
            swapped_word += character.lower()
    return swapped_word


if __name__ == "__main__":
    print(highlow(input()))
