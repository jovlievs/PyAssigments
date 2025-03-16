# 7. **Last Element**: Access the last element of a list, considering what to return if the list is empty.
mylist = list(map(int, input("Enter a list of numbers: ").split()))
print(mylist and f"Mylist's last number is {mylist[-1]}" or "Mylist is empty!")