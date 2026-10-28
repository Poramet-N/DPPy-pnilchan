#!/usr/bin/env python3

user_input = int(input("Please tell me your age: ").strip())

print(f"You are currently {user_input} years old.")

year = 10

while year <= 30:
    result = year + user_input
    print(f"In {year} years, you'll be {result} years old.")
    year += 10

    if year > 30:
        break


    
