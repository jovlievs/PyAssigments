# 1. Create a program to ask name and year of birth from user and tell them their age
name, birth = map(str, input("What is your name and birth year: ").split())
birth = int(birth)
print(f"You are {date.time.now - birth} years old!")
