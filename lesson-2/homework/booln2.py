# 2. Create a program that checks if two numbers are equal and outputs a message if they are
a, b = map(int, input("Enter two numbers: ").split())
res = int(a == b)
print(res * "Yes, they are" + int(not bool(res)) * "No, they aren't")