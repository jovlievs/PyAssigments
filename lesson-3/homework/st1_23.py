# 1. **Union of Sets**: Given two sets, create a new set that contains all unique elements from both sets.
# st1 = {3, 2, 4, 5}
# st2 = {5, 4, 8, 9, 0}

# print(st1.union(st2))

# 2. **Intersection of Sets**: Given two sets, create a new set that contains elements common to both sets.
# st1 = {3, 2, 4, 5}
# st2 = {5, 4, 8, 9, 0}

# print(st1.intersection(st2))

# 3. **Difference of Sets**: Given two sets, create a new set with elements from the first set that are not in the second.
# st1 = {3, 2, 4, 5}
# st2 = {5, 4, 8, 9, 0}

# print(st1.difference(st2))

# 4. **Check Subset**: Given two sets, check if one set is a subset of the other.
# st1 = {3, 2, 4, 5}
# st2 = {3, 2}

# print(st2.issubset(st1))

# 5. **Check Element**: Given a set and an element, check if the element exists in the set.
# st = {1, 2, 3, 4, 5}
# num = 4
# print(num in st)

# 6. **Set Length**: Determine the number of unique elements in a set.
# st = {1, 2, 2, 3, 3, 3, 4}
# print(len(st))

# 7. **Convert List to Set**: Given a list, create a new set that contains only the unique elements from that list.
# lst = [1, 2, 2, 3, 3, 3, 4]
# print(set(lst))

# 8. **Remove Element**: Given a set and an element, remove the element if it exists.
# st = {1, 2, 3, 4, 5, 6}
# num = 6
# st.remove(num)
# print(st)

# 9. **Clear Set**: Create a new empty set from an existing set.
# st1 = {1, 2, 3}
# st1.clear()
# print(st1)

# 10. **Check if Set is Empty**: Determine if a set has any elements.
# st = {1, 2, 3, 4}
# if st:
#     print("Not empty!")
# else:
#     print("Empty!")

# 11. **Symmetric Difference**: Given two sets, create a new set that contains elements that are in either set but not in both.
# st1 = {1, 2, 3, 4}
# st2 = {3, 4, 5, 6}

# print(st1.symmetric_difference(st2))

# 12. **Add Element**: Given a set and an element, add the element to the set if it is not already present.
# st1 = {1, 2, 3, 4, 5}
# num = 2
# st1.add(num)
# print(st1)

# 13. **Pop Element**: Given a set, remove and return an arbitrary / random element from the set.
# st1 = {2, 3, 4, 5}
# random_removed = st1.pop()
# print(random_removed)

# 14. **Find Maximum**: From a given set of numbers, find the maximum element.
# st1 = {1, 9, 2, 11, 0, -1, 1} 
# Sets are not subscriptible, that is, you cannot access the element by index
# so, you can sort it first, and then it is possible 
# st2 = sorted(st1)
# print(st2[-1])

# 15. **Find Minimum**: From a given set of numbers, find the minimum element.
# st1 = {1, 9, 2, 11, 0, -1, 1} 
# st2 = sorted(st1)
# print(st2[0])

# 16. **Filter Even Numbers**: Given a set of integers, create a new set that contains only the even numbers.
# st1 = {1, 2, 3, 4, 2, 4, 0, 8, 5}
# lst = list(st1)
# st2 = set(filter(lambda x : x % 2 == 0, lst))
# print(st2)

# 17. **Filter Odd Numbers**: Given a set of integers, create a new set that contains only the odd numbers.
# st1 = {1, 2, 3, 4, 2, 4, 0, 8, 5}
# lst = list(st1)
# st2 = set(filter(lambda x : x % 2 != 0, lst))
# print(st2)

# 18. **Create a Set of a Range**: Create a set of numbers in a specified range (e.g., from 1 to 10).
# st = set()
# for i in range(1, 11):
#     st.add(i)
# print(st)

# 19. **Merge and Deduplicate**: Given two lists, create a new set that merges both lists and removes duplicates.
# lst1 = [9, 8, 7, 6]
# lst2 = [7, 6, 11, 12]

# print((set(lst1).union(set(lst2))))

# 20. **Check Disjoint Sets**: Given two sets, check if they have no elements in common.
# st1 = {1, 2, 3, 4}
# st2 = {5, 6, 7, 8}

# bolean = st2.isdisjoint(st1)
# print(bolean)

# 21. **Remove Duplicates from a List**: Given a list, create a set from it to remove duplicates, then convert back to a list.
# lst = [2, 2, 3, 3, 4, 4, 6, 1]
# st = set(lst)
# print(list(st))

# 22. **Count Unique Elements**: Given a list, determine the count of unique elements using a set.
# def uniik(lst):
#     return [item for item in lst if lst.count(item) == 1]

# lst = [9, 2, 2, -1, -3, 4, 5, 3, 3]
# print(uniik(lst))

# 23. **Generate Random Set**: Create a set with a specified number of random integers within a certain range.
# start = 3
# end = 52
# st = set()

# for i in range(start, end):
#     st.add(i)
# print(st)

# import random

# start = 1
# end = 100
# cnt = 32

# st = set(random.sample(range(start,end + 1), min(cnt, end - start + 1)))
# print(st)