#!/usr/bin/env python3

import sys
import re

param_count = len(sys.argv) - 1

if param_count != 2:
    print("none")

else:
    param = re.findall(sys.argv[1],sys.argv[2])
    keyword_count = len(param)
    print(keyword_count)