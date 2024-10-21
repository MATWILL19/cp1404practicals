"""
CP1404/CP5632 - Practical
Answer the following questions:

1. When will a ValueError occur?
When a string is entered into the function

2. When will a ZeroDivisionError occur?
When you attempt to perform a division operation using zero as a denominator

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Python (Nor any calculator I know of) will not allow you to divide by zero
However we can set a boundry condition to prevent a user from inputting zero for the denominator in the first place
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")