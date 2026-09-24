original_numbers = [2, 8, 9, 48, 9, 22, -12, 2]
unique_incremented_numbers = []

for number in original_numbers:
    incremented_number = number + 2
    if number > 5 and incremented_number not in unique_incremented_numbers:
        unique_incremented_numbers.append(incremented_number)

print(unique_incremented_numbers)
