#!/usr/bin/env python3

num = [9, 5, 38, 89, 34, -34, 7, -10]

plus_num = [x + 2 for x in num if x > 5]

print(f"""{num}
{plus_num}""")