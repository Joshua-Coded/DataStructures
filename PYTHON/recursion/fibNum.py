# a program that prints fib numbers

# 1, 1, 2, 3, 5, 8, 13

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = fib(n -1) + fib(n -2)
        return result


# Ask for how many they want to find.
numFibValue = int(input("How many do you want to find?"))

# Loop while calling for each new number.
i = 1
while i < numFibValue:
    fibValue = fib(i)
    print(fibValue)
    i += 1

print("All done!")

# print result and increment.