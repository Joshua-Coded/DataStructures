oneTo10 = range(1, 11)

def dbl_num(num):
    return num * 2

print(list(map(dbl_num, oneTo10)))

print(list(map((lambda x: x * 3), oneTo10)))

aList = list(map((lambda x, y : x + y), [1, 2, 3], [2, 4, 7]))
print(aList)

print(list(filter((lambda x: x % 2 == 0), range(1, 11))))