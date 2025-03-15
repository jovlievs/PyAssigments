# 15. Ask the user for a sentence and create an acronym from the first letters of each word.  
#     Example:  
#     - Input: "World Health Organization"  
#     - Output: "WHO"  
word = input("Enter a word: ")
mylist = list(map(str, word.split()))
new_list = []
for i in range(0, len(mylist)):
    new_list.append(mylist[i][0])
print("".join(new_list))

