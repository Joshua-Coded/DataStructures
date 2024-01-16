# ------------ Problem ------------
# Generate a list of 50 random values between 1 and 1000
# and return those that are multiples of 9
# you will have to use a list comprehension in a list comprehension


# Solution

import random
print([x for x in [random.randint(1, 1001) for i in range(50)] if x % 9 == 0])