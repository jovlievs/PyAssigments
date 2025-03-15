# 7. Write a program that checks if the sum of two numbers is greater than 50.8. Create a program that checks if a given number is between 10 and 20 (inclusive)
a, b = map(int, input("Enter two words: ").split())
res = sum((a, b)) > 50.8
print(int(res) * "Yes" + int(not res) * "No")

c = int(input("Enter a number: "))
res = c >= 10 and c <= 20
print(int(res) * "Yes" + int(not res) * "No")