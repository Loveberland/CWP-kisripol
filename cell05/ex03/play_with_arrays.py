#include stdio.h
original_array = [2, 8, 9, 48, 9, 22, -12, 2]
new_array = []

for i in original_array:
    if i > 5 and (i+2) not in new_array:
        new_array.append(i+2)

print(new_array)
