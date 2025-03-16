# 11. **Remove Duplicates**: Given a list, create a new list that contains only unique elements from the original list.
gvn = [9, 1, 2, 3, 4, 1, 2, 3]
unique_list = []

for i in gvn:
    if i not in unique_list:
        unique_list.append(i)
print(unique_list)


