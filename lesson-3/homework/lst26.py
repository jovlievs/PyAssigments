# 26. **Get Middle Element**: Given a list, find the middle element. If the list has an even number of elements, return the two middle elements.

gv = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
mid = len(gv) // 2
print(mid, len(gv))
res = gv[mid - 1: mid + 1] if len(gv) % 2 == 0 else gv[mid]
print(res)