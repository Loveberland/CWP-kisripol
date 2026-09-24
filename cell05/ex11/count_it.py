import sys

print("parameters:", len(sys.argv))
for argument in sys.argv:
    print(f"{argument}: {len(argument)}")
