# 14. **Check for Empty List**: Determine if a list is empty and return a boolean.
lst = list(map(int, input('Enter a list of numbers: ').split()))
res = int(not lst)
print(res * "Empty!" + int(not bool(res)) * "Not empty!")