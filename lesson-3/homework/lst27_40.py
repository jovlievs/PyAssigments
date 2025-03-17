# 27. **Find Maximum of Sublist**: Given a list, find the maximum element of a specified sublist.
# gvn = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# start = 3
# end = 7
# print(gvn[start:end])
# print(max(gvn[start:end]))

# 28. **Find Minimum of Sublist**: Given a list, find the minimum element of a specified sublist.
# gvn = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# start = 3
# end = 7
# print(gvn[start:end])
# print(min(gvn[start:end]))

# 29. **Remove Element by Index**: Given a list and an index, remove the element at that index if it exists.
# ind = 8
# newl = []
# if 0 <= ind < len(gvn):
#     del gvn[ind] # gvn.pop(ind)
#     newl = gvn
# print(newl)

# 30. **Check if List is Sorted**: Determine if the list is sorted in ascending order and return a boolean.
# gvn = [1, 2, 3, 4, 5, 1]
# res = gvn == sorted(gvn)
# print(res)

    # 31. **Repeat Elements**: Given a list and a number, create a new list where each element is repeated that number of times.
# gvn = [1, 2, 3, 4, 5, 6, 7]
# num = 3

# newl = []
# for i in gvn:
#     for j in range(0, num):
#         newl.append(i)
# print(newl)

# lst = [1, 2, 3, 4, 5, 6, 7]
# new_list = []
# new_list.extend([item] * num for item in lst)  # Appending repeated elements
# print(sum(new_list, []))  # Flattening the nested lists

# 32. **Merge and Sort**: Given two lists, create a new sorted list that merges both lists.
# lst1 = [1, 2, 3, 4, 5]
# lst2 = [3, 4, 5, 6, 7]

# newl = lst1 + lst2
# print(sorted(newl))

# 33. **Find All Indices**: Given a list and an element, find all the indices of that element in the list.
# gvn = [1, 2, 3, 2, 3, 4, 2, 3, 2, 2, 2, 2, 9]
# num = 2
# cnt = 0
# for i in gvn:
#     if i == num:
#         cnt += 1
# print(f"{num} is repeated {cnt} times!")

# 34. **Rotate List**: Given a list, create a new list that is a rotated version of the original list (shift elements to the right).
# lst = [1, 2, 3, 4, 5]
# print(lst[-2:] + lst[:-2]) => [4, 5, 1, 2, 3]

# def rotate(lst, k):
#     k = k % len(lst)
#     return lst[-k:] + lst[:-k]

# gvn = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# num = 3
# rotated_new = rotate(gvn, num)
# print(rotated_new)

# 35. **Create Range List**: Create a list of numbers in a specified range (e.g., from 1 to 10).
# start = 1
# end = 10

# lst = list(range(start, end))
# print(lst)

# 36. **Sum of Positive Numbers**: Given a list of numbers, calculate the sum of all positive numbers.
# gvn = [1, 2, 3, 4, -1, -2, 3, 4]
# sm = 0
# for i in gvn:
#     if i > 0:
#         sm += i
# print(sm)

# 37. **Sum of Negative Numbers**: Given a list of numbers, calculate the sum of all negative numbers.
# gvn = [1, 2, 3, 4, -1, -2, 3, 4]
# sm = 0
# for i in gvn:
#      if i < 0:
#          sm += i
# print(sm)

# 38. **Check Palindrome**: Given a list, check if the list is a palindrome (reads the same forwards and backwards).
# gvn = [1, 2, 3, 4, 3, 2, 1]
# print(gvn == gvn[::-1])

# 39. **Create Nested List**: Create a new list that contains sublists, where each sublist contains a specified number of elements from the original list.
# gvn = [1, 2, 3, 4, 5, 6]
# nwl = [[gvn[i - 1], gvn[i]] for i in range(1, len(gvn) ,2)]
# print(nwl)

# 40. **Get Unique Elements in Order**: Given a list, create a new list that contains unique elements while maintaining the original order.
# gvn = [2, 9, 8, 7, 1, 2, 3, 2, 3, 4, 5, 6, 7, 4, 9]
# newl = []
# for i in gvn:
#     if not i in newl:
#         newl.append(i)
# print(newl)









