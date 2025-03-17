# 1. **Count Occurrences**: Given a tuple and an element, find how many times the element appears in the tuple.
# gvn = (1, 1, 1, 2, 3, 4)
# num = 1
# print(gvn.count(1))

# 2. **Max Element**: From a given tuple, determine the largest element.
# gvn = (9, -3, 4, 5, -3, 0, 11)
# print(max(gvn))

# 3. **Min Element**: From a given tuple, determine the smallest element.
# gvn = (-9, 1, 2, 3, 4, 5, 6, 7)
# print(min(gvn))

# 4. **Check Element**: Given a tuple and an element, check if the element is present in the tuple.
# gvn = (1, 2, 3, 4, 1, 3, 4, 9)
# num = -9
# print(num in gvn)

# 5. **First Element**: Access the first element of a tuple, considering what to return if the tuple is empty.
# gvn = tuple()
# if gvn:
#     print(gvn[0])
# else:
#     print("Your tuple is empty!")

# 6. **Last Element**: Access the last element of a tuple, considering what to return if the tuple is empty.
# gvn = tuple()
# if gvn:
#     print(gvn[-1])
# else:
#     print("Your tuple is empty!")

# 7. **Tuple Length**: Determine the number of elements in the tuple.
# gvn = (1, 2, 3, 4, 5)
# print(len(gvn))

# 8. **Slice Tuple**: Create a new tuple that contains only the first three elements of the original tuple.
# gvn = (1, 2, 3, 4, 5, 6)
# newtple = gvn[0:3]
# print(newtple)

# 9. **Concatenate Tuples**: Given two tuples, create a new tuple that combines both.
# tple1 = (1, 2, 3, 4, 5)
# tple2 = (4, 5, 6, 7, 8)

# tple3 = tple1 + tple2
# print(tple3)

# 10. **Check if Tuple is Empty**: Determine if a tuple has any elements.
# gvn = ()
# if gvn:
#     print("Not empty!")
# else:
#     print("Empty!")

# 11. **Get All Indices of Element**: Given a tuple and an element, find all the indices of that element in the tuple.
# tple = (1, 2, 3, 2, 2, 2, 3, 4, 2)
# num = 2
# lst = []
# for i in range(len(tple)):
#     if tple[i] == num:
#         lst.append(i)
# print(lst)

# 12. **Find Second Largest**: From a given tuple, find the second largest element.
# tple = (4, 3, -9, 5, 6, -1, 0)
# tple2 = sorted(tple)
# print(tple2[-2])

# 13. **Find Second Smallest**: From a given tuple, find the second smallest element.
# tple = (4, 3, -9, 5, 6, -1, 0)
# tple2 = sorted(tple)
# print(tple2[1])

# 14. **Create a Single Element Tuple**: Create a tuple that contains a single specified element.
# element = int(input("Enter a number: "))
# tple = (element,)

# print(type(tple))
# print(tple)

# 15. **Convert List to Tuple**: Given a list, create a tuple containing the same elements.
# lst = [1, 3, 5, 7, 8]
# tple = tuple(lst)
# print(type(tple), tple)

# 16. **Check if Tuple is Sorted**: Determine if the tuple is sorted in ascending order and return a boolean.
# tple = (1, 2, 3, 4, 5)
# print(tple == tuple(sorted(tple)))

# 17. **Find Maximum of Subtuple**: Given a tuple, find the maximum element of a specified subtuple.
# start = 2
# end = 5
# tple = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# print(max(tple[start:end + 1]))

# 18. **Find Minimum of Subtuple**: Given a tuple, find the minimum element of a specified subtuple.
# start = 2
# end = 5
# tple = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# print(min(tple[start:end + 1]))

# 19. **Remove Element by Value**: Given a tuple and an element, create a new tuple that removes the first occurrence of that element.
# tple = (1, 2, 3, 2, 3, 2, 3)
# num = 2
# lst = list(tple)
# ind = lst.index(num)
# lst.pop(ind) # del lst[ind]
# tple2 = tuple(lst)
# print(tple2)

# tple = (1, 2, 3, 2, 3, 2, 3)
# num = 2
# tple2 = tuple(x for i, x in enumerate(tple) if i != tple.index(num)) => enumerate(iterable, start) => (index, value)
# print(tple2)

# tple = ('a', 'b', 'c')

# for index, value in enumerate(tple):
#     print(index, value)

# 20. **Create Nested Tuple**: Create a new tuple that contains subtuples, where each subtuple contains specified elements from the original tuple.
# tple1 = (1, 2, 3, 4, 5, 6, 7)
# lst1 = list(tple1)

# lst2 = list((lst1[i - 1], lst1[i]) for i in range(0, len(lst1), 2))
# print(tuple(lst2))

# 21. **Repeat Elements**: Given a tuple and a number, create a new tuple where each element is repeated that number of times.
# tple = (1, 2, 3, 4, 5, 6, 7)
# num = 2
# lst = list(tple)
# new_list = []
# for i in lst:
#     for j in range(num):
#         new_list.append(i)

# print(tuple(new_list))

# 22. **Create Range Tuple**: Create a tuple of numbers in a specified range (e.g., from 1 to 10).
# lst = []
# for i in range(1, 11):
#     lst.append(i)
# print(tuple(lst))

# 23. **Reverse Tuple**: Create a new tuple that contains the elements of the original tuple in reverse order.
# tple = (1, 2, 3, 4, 3, 2)
# lst = list(tple)
# print(tuple(reversed(lst)))

# 24. **Check Palindrome**: Given a tuple, check if the tuple is a palindrome (reads the same forwards and backwards).
# tple = (1, 2, 3, 0, 2, 1)
# print(tple == tple[::-1])

# 25. **Get Unique Elements**: Given a tuple, create a new tuple that contains only the unique elements while maintaining the original order.
# tple = (9, 2, 9, 2, 3, 3, 0, 1, 1, 3, 4, 5, 6, 6, 5, 4)
# lst = list(tple)
# new_list = []
# for i in lst:
#     if i not in new_list:
#         new_list.append(i)

# print(tuple(new_list))


