# 19. **Replace Element**: Given a list, replace the first occurrence of a specified element with another element.
gvn = [1, 2, 3, 4, 5, 2]
old = 2
new = 100
itr = gvn.index(old)
gvn[itr] = new
print(gvn)

