#!/usr/bin/env python3

user_input = int(round(float(input("Enter a number : "))))

start_number = 0

while start_number <= 12 :
    print(f"{start_number} * {user_input} = {start_number * user_input}")
    start_number += 1