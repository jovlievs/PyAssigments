# 15. **Count Even Numbers**: Given a list of integers, count how many of them are even.
gvn = [1, 2, 3, 4, 5, 6]
cnt = 0
for i in gvn:
    if i % 2 == 0:
        cnt += 1
print(cnt)