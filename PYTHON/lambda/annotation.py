def random_func(name: str, age: int, weight: float) -> str:
    print("Name:", name)
    print("Age:", age)
    print("Weight:", weight)

    return "{} is {} years old and weighs {}".format(name, age, weight)

print(random_func("Joshua", 16, 154.6))

print(random_func("Victor", 17, 164.6))

print(random_func(16, "Joshua", 154.6))

print(random_func.__annotations__)