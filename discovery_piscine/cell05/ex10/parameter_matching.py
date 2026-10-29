#!/usr/bin/env python3

import sys

param_count = len(sys.argv) - 1

if param_count != 1:
    print("none")

else:
    user_input = input("What was the parameter? ").strip()

    if user_input == sys.argv[1]:
        print("Good job!")

    else:
        print("Nope, sorry...")

