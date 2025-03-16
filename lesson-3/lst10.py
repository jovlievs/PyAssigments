# 10. **Sort List**: Create a new list that contains the elements of the original list in sorted order.
gvn = ['aaa', 'aa', 'aaaaa', 'b', 'a', 'b']
print((sorted(gvn, key = lambda x: len(x))))
print((sorted(gvn, key = len)))
