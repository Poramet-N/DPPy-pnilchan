#!/usr/bin/env python3

first_number = float(input("Enter the first number: ").strip())
second_number = float(input("Enter the second number: ").strip())

answer1 = f"{first_number} * {second_number} = {first_number * second_number}"
answer2 = first_number * second_number 

print(f"{answer1}\n{answer2}")

if answer2 < 0 :
    print("The result is negative.")

elif answer2 > 0 :
    print("The result is positive.")

elif answer2 == 0 : 
    print("The result is negative and positive")
