# 5. Create a program that accepts two strings and checks if they have the same length.
a, b = map(str, input("Enter two words: ").split())

res = len(a) == len(b)
print(int(res) * "Yes!" + int(not res) * "No!")