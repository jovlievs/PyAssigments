# 4. Write a program that takes three numbers and checks if all of them are different.
a, b, c = map(int, input("Enter three numbers: ").split())
res = a == b and b == c
print(int(res) * "Yes, they are!" + int(not res) * "No, they aren't!")