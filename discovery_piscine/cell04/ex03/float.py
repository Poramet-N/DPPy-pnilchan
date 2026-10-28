#!/usr/bin/env python

user_input = float(input("Give me a number: ").strip())

if user_input % 1 == 0:
    print("This number in an integer.")

else:
    print("This number in an decimal.")