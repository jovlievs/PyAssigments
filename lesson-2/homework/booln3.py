# 3. Write a program that checks if a number is positive and even.
num = int(input("Enter a number: "))
res = num > 0 and num % 2 == 0
print(int(res) * f"Yes, {num} is both positive and even" + int(not res) * f"No, {num} is not!")