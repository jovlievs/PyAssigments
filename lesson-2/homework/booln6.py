# 6. Create a program that accepts a number and checks if it’s divisible by both 3 and 5.
num = int(input("Enter a number: "))
res = not num % 15
print(int(res) * "Yes" + int(not res) * "No")