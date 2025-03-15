# 6. Write a Python program to check if one string contains another.
a, b = map(str, input("Enter two words separately: ").split())
ans = a.find(f"{b}")
last_ans = int(ans > 0) * 'Yes' + int(ans < 0) * 'No'
print(last_ans)