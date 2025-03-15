# 12. Write a program that takes a list of words and joins them into a single string, separated by a character (e.g., - or ,).  
my_list = list(map(str, input("Enter list of words: ").split()))
print(my_list)
result = ' '.join(my_list)
print(result)