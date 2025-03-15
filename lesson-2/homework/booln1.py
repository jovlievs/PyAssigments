# 1. Write a program that accepts a username and password and checks if both are not empty.
a = input('Your name: ')
b = input('Your surname: ')
if a:
    print(f"Your name is {a}")
else:
    print("Name is not given!")
if b: 
    print(f"Your surname is {b}")
else:
    print("Surname is not given")