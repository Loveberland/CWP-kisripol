import sys

arguments_list = sys.argv
arguments_list.pop(0)
words_with_suffix = []
for argument in arguments_list:
    if not argument.endswith("ism"):
        words_with_suffix.append(argument + "ism")
print("\n".join(words_with_suffix))
