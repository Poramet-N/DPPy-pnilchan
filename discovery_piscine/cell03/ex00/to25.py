#!/usr/bin/env python3

user_input = round(float(input("Enter the number less then 25 : ").strip()))

if user_input > 25:
    print("Error")

while user_input <= 25:
    print(f"Inside the loop, my variable is{user_input}")
    user_input += 1
    if user_input > 25:
        break
    