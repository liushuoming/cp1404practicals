"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
   A ValueError will occur if the user enters something that cannot be converted to an integer,such as a letter or a string like "abc".
2. When will a ZeroDivisionError occur?
   A ZeroDivisionError will occur if the user enters 0 as the denominator.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    Yes, you can use a while loop to repeatedly prompt the user until they enter a non-zero denominator.
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