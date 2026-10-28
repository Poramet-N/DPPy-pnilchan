#!/usr/bin/env python3

password = "Python is awesom"

login = input().strip()

if login == password:
    print("ACCESS GRANTED")

else: 
    print("ACCESS DENIED")