double = (x * 2 for x in range(10))

print("Double : ", next(double))
print("Double : ", next(double))

for num in double:
    print(num)