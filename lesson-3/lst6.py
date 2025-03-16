# 6. **First Element**: Access the first element of a list, considering what to return if the list is empty.
mylist = list(map(int, input('Enter a list of numbers: ').split()))
print(mylist and f"Your list's first element is {mylist[0]}" or "Your list is empty!")

# print(a and b) print will check till end if given numbers are not null, if any of them is NULL, it prints NULL
# print(a or b) print will check 1st satisfied number(True) and abandon the rest of the part

