#!/usr/bin/env python3

import sys

param_count = len(sys.argv) - 1

if param_count < 2:
    print("none")

else:
    print(*sys.argv[:0:-1], sep="\n")