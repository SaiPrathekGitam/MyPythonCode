# Program to illustrate command line arguments

import sys

if len(sys.argv) < 2:
    print("Missing Number")
    sys.exit(1)

print(sys.argv[0])
