# 14. Write a program to ask for two strings and check if they are equal or not.  
a, b = map(str, input('Enter two words separately: ').split())
itr = a.find(b)
qym = itr > -1 and len(a) == len(b)
# print(qym)
result = int(qym) * "Yes" + int(qym == 0)* "No"
print(result)