#!/usr/bin/env python3

row = 0

while row <=10:
    print(f"Table de {row}", end=" ")

    column = 0

    while column <=10:
        result = row * column
        print(f"{result}", end=" ")
        column +=1

    print()
    row +=1