# 1. Create a program to ask name and year of birth from user and tell them their age
from datetime import datetime


name, birth = map(str, input("What is your name and birth year: ").split())
birth = int(birth)
print(f"You are {datetime.now().year - birth} years old!")
