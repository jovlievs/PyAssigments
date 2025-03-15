# Write a Python file that asks for three numbers and outputs the largest and smallest.
a = int(input('Enter your 1st number: '))
b = int(input('Enter your 2nd number: '))
c = int(input('Enter your 3rd number: '))

mx = max(max(a, b), c)
mn = min(min(a, b), c)

print(f"Max = {mx} and Min = {mn}")
