# 25. **Create a Copy**: Create a new list that is a copy of the original list.
from copy import deepcopy
old = [1, 2, 3, 4, 5]
new = old.copy()
print(new)
old.append(6)
print(old)

old1 = [
    [1, 2], 
    [4, 5]
]

new1 = deepcopy(old1) # If .copy() was used, it check it only shallow, not deep and result in referencing if the date in the list not primitive
old1[0].append(3)

print(new1)
print(old1)

