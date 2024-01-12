# import random
from functiontools import reduce

# randList = list(random.randint(1, 1001), for in range(100))

# print(list(filter(lambda x: x % 9 == 0), randList))

print(reduce((lambda x, y: x + y), range(1,6)))