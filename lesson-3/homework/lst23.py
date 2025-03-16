# 23. **Filter Odd Numbers**: Given a list of integers, create a new list that contains only the odd numbers.
gvn = [1, 2, 3, 4, 5, 6, 7]
odd_l = list(filter(lambda x: x % 2 == 1, gvn))
print("Odd numbers", odd_l)