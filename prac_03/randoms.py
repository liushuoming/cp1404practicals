import random

# Line 1
print(random.randint(5, 20))
# This generates a random integer between 5 and 20 (inclusive).
# Smallest possible: 5
# Largest possible: 20

# Line 2
print(random.randrange(3, 10, 2))
# This generates a random integer from the range 3 to 9 with a step of 2.
# Valid values: 3, 5, 7, 9
# Smallest possible: 3
# Largest possible: 9
# Could it have produced a 4? No — 4 is not in the range(3, 10, 2)

# Line 3
print(random.uniform(2.5, 5.5))
# This generates a random floating-point number between 2.5 and 5.5.
# Smallest possible (in theory): 2.5
# Largest possible (in theory): 5.5
# Values will be decimals and different on every run.

# Random number between 1 and 100 (inclusive)
random_number = random.randint(1, 100)
print(random_number)