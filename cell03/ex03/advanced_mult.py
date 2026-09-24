def advance_mult(max_table, max_multiplier):
    for table_number in range(max_table + 1):
        if table_number != 0:
            print()
        print(f"Table de {table_number}: ", end="")
        for multiplier in range(max_multiplier + 1):
            print(f"{table_number * multiplier}", end=" ")


if __name__ == "__main__":
    advance_mult(10, 10)
