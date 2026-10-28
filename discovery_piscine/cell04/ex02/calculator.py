#!/usr/bin/env python3

def input_num(val):
    num = float(val)
    return int(num) if num % 1 == 0 else num

first_num = input_num(input("Give me the first number: ").strip())
second_num = input_num(input("Give me the second number: ").strip())

addition = first_num + second_num
subtraction = first_num - second_num
division = first_num / second_num
multiplication = first_num * second_num

print(f"""Thank you!
{first_num} + {second_num} = {addition}
{first_num} - {second_num} = {subtraction}
{first_num} / {second_num} = {division}
{first_num} * {second_num} = {multiplication}""")


