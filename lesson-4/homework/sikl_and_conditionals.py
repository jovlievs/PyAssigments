## Questions:

# 1. <a href="https://pynative.com/python-if-else-and-for-loop-quiz/">Loops quiz</a>
# 2.  What is the difference between the continue and break statements in Python?
# 3. Can you explain the difference between for loop and while loop?
# 4. How would you implement a nested for loop system? Provide an example.

# ## Homeworks:

# **1.** Return uncommon elements of lists. Order of elements does not matter.
# ```
# input:
#     list1 = [1, 1, 2]
#     list2 = [2, 3, 4]
# output: [1, 1, 3, 4]
# ```

# ```
# input:
#     list1 = [1, 2, 3]
#     list2 = [4, 5, 6]
# output: [1, 2, 3, 4, 5, 6]
# ```

# ```
# input:
#     list1 = [1, 1, 2, 3, 4, 2]
#     list2 = [1, 3, 4, 5]
# output: [2, 2, 5]
# ```

# 1st approach
# lst1 = list(map(int, input('Enter your 1st list: ').split()))
# lst2 = list(map(int, input('Enter your 2nd list: ').split()))

# newlist = lst1 + lst2
# print(lst1, lst2)
# for i in range(len(lst1)):
#     for j in range(len(lst2)):
#         if lst2[j] in lst1:
#             newlist = [x for x in newlist if x != lst2[j]]
# print(newlist)

# 2nd approach
# lst1 = list(map(int, input('Enter your 1st list: ').split()))
# lst2 = list(map(int, input('Enter your 2nd list: ').split()))

# print([x for x in lst1 if x not in lst2] + [x for x in lst2 if x not in lst1])
        

# **2.** Print the square of each number which is less than `n` on a separate line.

# ```
# input: n = 5
# output:
#     1
#     4
#     9
#     16
# ```

# n = int(input('Enter a number: '))
# for i in range(n):
#     print(i * i)

# **3.** `txt` nomli string saqlovchi o'zgaruvchi berilgan. `txt`dagi har uchinchi belgidan keyin pastgi chiziqcha (underscore) qo'yilsin. 
# Agar belgi unli harf yoki orqasidan ostki chiziqcha qo'yilgan harf bo'lsa, ostki chiziqcha keyingi harfdan keyin qo'yilsin.
# Agar belgi satrdagi oxirgi belgi bo'lsa chiziqcha qo'yilmasin.

# ```
# input: hello
# output: hel_lo
# ```

# ```
# input: assalom
# output: ass_alom
# ```

# ```
# input: abcabcdabcdeabcdefabcdefg
# output: abc_abcd_abcdeab_cdef_abcdefg
# ```

# def add_underscore(word):
#     limited_letters = 'aeoiu'
#     cnt = 0
#     ans = ''

#     for i in range(len(word)):
#         cnt += 1
#         ans += word[i]
#         if i != len(word) - 1 and cnt >= 3 and word[i] not in limited_letters:
#             ans += '_'
#             limited_letters += word[i]
#             cnt = 0
#     return ans

# txt = input('Enter a word: ')
# print(add_underscore(txt))

# **4. Number Guessing Game**
# Create a simple number guessing game.
# - The computer randomly selects a number between 1 and 100. 
# - If the guess is high, print "Too high!". 
# - If the guess is low, print "Too low!". 
# - If they guess correctly, print "You guessed it right!" and exit the loop.
# - The player has 10 attempts to guess it. If the player can not find the correct number in 10 attempts, print "You lost. Want to play again? ".
# - If the player types one of 'Y', 'YES', 'y', 'yes', 'ok' then start the game from the beginning.

# > Hint: Use Python’s `random.randint()` to generate the number.

# import random

# def play_game():
#     while True:  # Keep playing if the user wants
#         secret_number = random.randint(1, 100)  # Random number between 1 and 100
#         attempts = 10  # Max attempts
#         lower_bound = 1
#         upper_bound = 100

#         print("\n🔢 Welcome to the Number Guessing Game!")
#         print("I have selected a number between 1 and 100. You have 10 attempts to guess it.")

#         for attempt in range(1, attempts + 1):
#             print(f"\nCurrent range: [{lower_bound}; {upper_bound}]")
#             try:
#                 guess = int(input(f"Attempt {attempt}/{attempts}: Enter your guess: "))

#                 if guess < lower_bound or guess > upper_bound:
#                     print(f"⚠️ Out of range! Please enter a number between {lower_bound} and {upper_bound}.")
#                     continue  # Skip the rest of the loop and ask for input again

#                 if guess < secret_number:
#                     print("📉 Too low!")
#                     lower_bound = max(lower_bound, guess + 1)  # Update lower bound
#                 elif guess > secret_number:
#                     print("📈 Too high!")
#                     upper_bound = min(upper_bound, guess - 1)  # Update upper bound
#                 else:
#                     print("🎉 You guessed it right! Congratulations! 🎉")
#                     break  # Exit loop if guessed correctly

#             except ValueError:
#                 print("⚠️ Invalid input! Please enter a number.")

#         else:  # If loop completes without a correct guess
#             print(f"❌ You lost! The correct number was {secret_number}.")

#         # Ask for replay
#         again = input("Want to play again? (yes/Y/ok): ").strip().lower()
#         if again not in ('y', 'yes', 'ok'):
#             print("Thanks for playing! Goodbye! 👋")
#             break  # Exit the game

# # Run the game
# play_game()


# **5. Password Checker**
# Task: Create a simple password checker.
# - Ask the user to enter a password. 
# - If the password is shorter than 8 characters, print "Password is too short." 
# - If the password doesn’t contain at least one uppercase letter, print "Password must contain an uppercase letter.". 
# - If the password meets both criteria, print "Password is strong."

# password = input('Enter a password: ')

# upper = 'ASDFGHJKLZXCVBNMQWERTYUIOP'
# if len(password) < 8:
#     print('Your password is too short! It should be at least 8 characters!')
# else:
#     if not any(char.isupper() for char in password):
#         print('Your password need to has at least one UpperCase letter!')
#     else:
#         print('Your password is approved!')

# **6. Prime Numbers**
# Task: Write a Python program that prints all prime numbers between 1 and 100.

# > A prime number is a number greater than 1 that is not divisible by any number other than 1 and itself. Use nested loops to check divisibility.

# ---

# from math import sqrt


# def isPrime(num):
#     if num < 2:
#         return False
#     else:
#         for i in range(2, int(sqrt(num)) + 1):
#             if num % i == 0:
#                 return False
#     return True

# def how_many_primes_to_n(n):
#     list_of_them = []
#     for i in range(2, n + 1):
#         if isPrime(i):
#             list_of_them.append(i)
    
#     return list_of_them

# n = int(input('Enter a number: '))
# print(f"A list of prime numbers to {n}: {how_many_primes_to_n(n)}")


# ### Bonus Challenge
# Task: Create a simple text-based Rock, Paper, Scissors game where the player plays against the computer.
# - The computer randomly chooses `rock`, `paper`, or `scissors` using `random.choice()`.
# - The player enters their choice.
# - Display the winner and keep track of scores for the player and the computer.
# - First to 5 points wins the match.

import random

comp_res = 0
person_res = 0
score = 5

while max(person_res, comp_res) < 5:

    message = input("Choose one of them: [rock, paper, scissors] ").lower()
    if message not in ['rock', 'paper', 'scissors']:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        continue

    option = random.choice(['rock', 'paper', 'scissors'])

    if message == option:
        print("Draw!")
    elif (message == "rock" and option == "scissors") or \
         (message == "paper" and option == "rock") or \
         (message == "scissors" and option == "paper"):
        person_res += 1
        print(f"You win this round! Scoreboard: [You - {person_res} : {comp_res} - Computer]")
    else:
        comp_res += 1
        print(f"Computer wins this round! Scoreboard: [You - {person_res} : {comp_res} - Computer]")

if person_res > comp_res:
    print("You won the game!")
elif person_res < comp_res:
    print("Computer won the game!")
else:
    print("Draw! It is a good play with you!")


 







