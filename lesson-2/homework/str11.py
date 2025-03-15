# 11. Write a program to check if a string contains any digits. 
wrd = input('Enter anything string: ')
checker = any(element.isdigit() for element in wrd)
print(checker)
