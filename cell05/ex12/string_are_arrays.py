import sys
z_count = 0 
for i in sys.argv[1]:
    if i == "z":
        z_count += 1
print("z"*z_count)
