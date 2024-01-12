def is_digit_odd(num):
    if num  % 2 == 0:
        return False
    else:
        return True


def change_list(list, func):

    oddList = []

    for i in list:
        if func(i):
            oddList.append(i)
    return oddList

aList = range(1, 20)

print(change_list(aList, is_digit_odd))