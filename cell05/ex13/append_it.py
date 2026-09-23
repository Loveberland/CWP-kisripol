import sys
arguments_list = sys.argv
arguments_list.pop(0)
modified_list = []
for i in arguments_list:
    if i[-3:] != "ism":
        modified_list.append(i+"ism")
print("\n".join(modified_list))
