# from collections import Counter

# word = input("Enter a word: ").lower()  # Convert to lowercase for uniformity
# vowels = "aeiou"

# # Count occurrences of characters
# char_count = Counter(word)

# # Count vowels using sum and filter
# vowel_count = sum(map(char_count.get, filter(vowels.__contains__, word)))

# # Total letters minus vowel count gives consonant count
# consonant_count = sum(char_count.values()) - vowel_count  

# print("Vowels:", vowel_count)
# print("Consonants:", consonant_count)

lst=input() 
print(len(list(filter(lambda x: x in ['a','e','u','i','y','o'], lst))))