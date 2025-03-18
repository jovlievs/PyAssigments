# ### Dictionary Tasks

# 1. **Get Value**: Given a dictionary and a key, retrieve the associated value, considering what to return if the key doesn’t exist.
# staff = {
#     'name': 'John',
#     'surname': 'Doe',
#     'age': '23',
#     'phone': 998971234567
# }

# key = 'age'
# if key in staff:
#     print(staff[key])
# else:
#     print(f"{key} - key is not found!")

# 2. **Check Key**: Given a dictionary and a key, check if the key is present in the dictionary.
# staff = {
#     'name': 'John',
#     'surname': 'Doe',
#     'age': '23',
#     'phone': 998971234567
# }

# key = 'age'
# if key in staff:
#     print(f"{key} is found in the dict!")
# else:
#     print(f"{key} is not found in the dict")

# 3. **Count Keys**: Determine the number of keys in the dictionary.
# staff = {
#     'name': 'John',
#     'surname': 'Doe',
#     'age': '23',
#     'phone': 998971234567
# }

# print(len(staff.keys()))

# 4. **Get All Keys**: Create a list that contains all the keys in the dictionary.
# staff = {
#     'name': 'John',
#     'surname': 'Doe',
#     'age': '23',
#     'phone': 998971234567
# }

# print(list(staff.keys()))

# 5. **Get All Values**: Create a list that contains all the values in the dictionary.
# staff = {
#     'name': 'John',
#     'surname': 'Doe',
#     'age': '23',
#     'phone': 998971234567
# }

# print(list(staff.values()))

# 6. **Merge Dictionaries**: Given two dictionaries, create a new dictionary that combines both.
# dad = {
#     'dad': 'John',
#     'dad_occupation': 'IT engineer',
#     'dad_age': '37'
# }

# mum = {
#     'mum': 'Lisa',
#     'mum_occupation': 'Data engineer',
#     'mum_age': '33'
# }

# dad.update(mum)
# family = dad.copy()
# print(family)

# 7. **Remove Key**: Given a dictionary and a key, remove the key if it exists, handling the case if it doesn’t.
# def rmv(dict, key):
#     dict.pop(key, None)
#     return dict

# staff = {
#     'name': 'John',
#     'surname': 'Doe',
#     'age': '23',
#     'phone': 998971234567
# }
# key = 'age'
# print(rmv(staff, key))

# 8. **Clear Dictionary**: Create a new empty dictionary.
# new_dict = dict()
# print(new_dict)

# 9. **Check if Dictionary is Empty**: Determine if a dictionary has any elements.
# dct = {1: 'a', 2: 'b', 3: 'c'}
# dct = dict()
# if dct:
#     print(dct)
# else:
#     print('Dict is empty!')

# 10. **Get Key-Value Pair**: Given a dictionary and a key, retrieve the key-value pair if the key exists.
# dct = {1: 'a', 2: 'b', 3: 'c'}
# key = 5
# if key in dct:  
#     lst = [key, dct[key]]
#     print(lst)  
# else:
#     print(f"Key {key} not found.")

# 11. **Update Value**: Given a dictionary, update the value for a specified key.
# person = {
#     'name': 'John',
#     'surname': 'Doe',
#     'email': 'john@gmail.com'
# }

# key = 'email'
# person[key] = 'jooohn@gmail.com'
# print(person)

# 12. **Count Value Occurrences**: Given a dictionary, count how many times a specific value appears across the keys.
# dc = {1: 'a', 2: 'b', 3: 'a', 4: 'a', 5: 'c'}
# value = 'a'

# ls_values = list(dc.values())
# print(ls_values)
# print(ls_values.count(value))
      
# 13. **Invert Dictionary**: Given a dictionary, create a new dictionary that swaps keys and values.
# def invert_dict(dict):
#     return {value: key for key, value in dict.items()}

# dc = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
# print(invert_dict(dc))

# 14. **Find Keys with Value**: Given a dictionary and a value, create a list of all keys that have that value.
# def new_dict(dct, value):

#     return [key for key, val in dct.items() if val == value]

# dc = {1: 'a', 2: 'b', 3: 'a', 4: 'd', 5: 'e'}
# value = 'a'
# print(new_dict(dc, value)) 

# 15. **Create a Dictionary from Lists**: Given two lists (one of keys and one of values), create a dictionary that pairs them.
# keys = [1, 2, 3, 4]
# values = ['a', 'b', 'c', 'd']

# print(dict(zip(keys, values)))
# dc = {key: value for key, value in zip(keys, values)}
# print(dc)

# 16. **Check for Nested Dictionaries**: Given a dictionary, check if any values are also dictionaries.

# def checknested(dct):
#     return any(isinstance(value, dict) for value in dct.values())

# dc1 = {
#     'bank_acc': 'a',
#     # 'bank_acc1': {
#     #     1: '$100,000',
#     #     2: '$200,000',
#     #     3: '$300,000'
#     # },
#     'business_acc': '$150,000'
# }

# print(checknested(dc1))


# 17. **Get Nested Value**: Given a nested dictionary, retrieve a value from within one of the inner dictionaries.
# dc = {1:{1:'a'}, 2:'b', 3: {7: 'c'}}
# print(dc[3][7])

# 18. **Create Default Dictionary**: Create a dictionary that provides a default value for missing keys.
# from collections import defaultdict

# # person = defaultdict(list)
# person = {}

# person['name'] = 'John'
# # skills = person.get('skills')
# # if not skills:
# #     person['skills'] = []

# person.setdefault('skills', []).append('C#')

# person['skills'].append('python')
# person['skills'].append('writing')

# print(person['skills'])

# 19. **Count Unique Values**: Given a dictionary, determine the number of unique values it contains.
# dc = {1: 'a', 2: 'b', 3: 'a', 4: 'a', 5: 'c', 7: {'p'}}

# lst = list(dc.values())
# print(lst)
# cnt = 0
# for i in lst:
#     if lst.count(i) == 1:
#         cnt += 1
# print(cnt)

# 20. **Sort Dictionary by Key**: Create a new dictionary sorted by keys.
# dct = {9: 'a', 8: 'b', 7: 'c', 6: 'd', 5: 'e'}

# new_dic = dict(sorted(dct.items()))
# print(new_dic)

# 21. **Sort Dictionary by Value**: Create a new dictionary sorted by values.
# dct = {5: 'e', 6: 'd', 7: 'c', 8: 'b', 9: 'a'}

# res = dict(sorted(dct.items(), key = lambda item : item[1]))
# print(res)

# 22. **Filter by Value**: Given a dictionary, create a new dictionary that only includes items with values that meet a certain condition.
# dct = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

# new_dict = dict(filter(lambda item: item[1] % 3 == 0, dct.items()))
# print(new_dict)

# 23. **Check for Common Keys**: Given two dictionaries, check if they have any keys in common.
# dct1 = {1: 'a', 2: 'c', 3: 'b'}
# dct2 = {3: 'e', -1: 'ng'}

# k1 = set(dct1.keys())
# k2 = set(dct2.keys())

# if not k1.intersection(k2):
#     print("Not common keys!")
# else:
#     print(f"{k1.intersection(k2)} is common key!")


# 24. **Create Dictionary from Tuple**: Given a tuple of key-value pairs, create a dictionary from it.
# tple = ((1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'))

# dct = dict(tple)
# print(dct)

# 25. **Get the First Key-Value Pair**: Retrieve the first key-value pair from a dictionary.
# dct = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

# res = list(dct.items())
# print(res[0])