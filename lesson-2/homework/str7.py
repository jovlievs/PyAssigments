# 7. Ask the user to input a sentence and a word to replace. Replace that word with another word provided by the user.  
# Example:  
#    - Input sentence: "I love apples."  
#    - Replace: "apples"  
#    - With: "oranges"  
#    - Output: "I love oranges."
a = input('Enter a simple sentence: ')
b, c = map(str, input('1st word should be in sentence above and 2nd word is you want to replace, please enter them separately: ').split())

ans = a.replace(f"{b}", f"{c}")
print(ans)