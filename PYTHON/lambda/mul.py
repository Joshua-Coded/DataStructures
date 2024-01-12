def mult_by_2(num):
    return num * 2

def do_math(func, num):
    return func(num)

print(" 8 * 2 = ", do_math(mult_by_2, 8))
times_two = mult_by_2

print(" 3 * 2 = ", times_two(3))

def get_func_mult_by_num(num):


    def mult_by(value):
        return num * value

    return mult_by

generated_func = get_func_mult_by_num(5)
print("5 * 10 = ", generated_func(10))


listOfFuncs = [times_two, generated_func]
print("5 * 9 = ", listOfFuncs[1](9))