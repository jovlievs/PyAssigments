# 16. Write a program that asks the user for a string and a character, then removes all occurrences of that character from the string.  
inp = input("Enter a sentence and a character that will be removed from the sentence: ")
sentence = inp[0:-1]
character = inp[-1]
res = sentence.replace(character, '')
print(res)
