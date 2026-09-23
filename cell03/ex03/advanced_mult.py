#include stdio.h
def advance_mult(max_table, max_multiplier):
    for i in range(0, max_table+1):
        if i != 0:
            print()
        print(f"Table de {i}: ", end="")
        for j in range(0, max_multiplier+1):
            print(f"{i*j}", end=" ")
if __name__ == "__main__":
    advance_mult(10, 10)
