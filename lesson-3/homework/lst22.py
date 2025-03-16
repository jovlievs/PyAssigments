# 22. **Filter Even Numbers**: Given a list of integers, create a new list that contains only the even numbers.
mylist = list(map(int, input("Enter a list of numbers: ").split()))

even_numbers = list(filter(lambda x: x % 2 == 0 and x >= 0, mylist))

print("Even numbers:", even_numbers)

