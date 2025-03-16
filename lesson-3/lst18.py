# 18. **Find Sublist**: Given a list and a sublist, check if the sublist exists within the list.
a = [1, 2, 3, 4, 5]
b = [1, 2, 0]

res = str(b)[1:-1] in str(a)[1:-1]
print(res)
