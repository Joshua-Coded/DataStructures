# lambda args1, arg2, .... : expression

# sum = lambda x, y : x + y

# print("Sum : ", sum(4, 5))

# can_vote = lambda age: True if age >= 18 else False
# print("Can_Vote : ", can_vote(19))

# powerList = [lambda x: x ** 2,
#                  lambda x : x ** 3,
#                  lambda x : x ** 4]


# for func in powerList:
#     print(func(4))

attack = {
    "quick" : (lambda: print("Quick Attack")),
    "power" : (lambda: print("Power Attack")),
    "miss" : (lambda: print("Miss Attack")),
        }

attack["quick"]()

import random

attackKey = random.choice(list(attack.keys()))

attack[attackKey]()