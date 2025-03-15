# 18. Write a program that checks if a string starts with one word and ends with another.  
#     Example:  
#     - Input: "Python is fun!"  
#     - Starts with: "Python"  
#     - Ends with: "fun!" 
inp = input("Enter a sentence: ")
mylist = list(map(str, inp.split()))

res = int(mylist[0] == mylist[-1])
last_res = (res & 1) * f"The beginning and the end of the sentence is the same: {mylist[0]}" + int(( not bool(res))) * f"They are different: {mylist[0]} and {mylist[-1]}" 
print(last_res)