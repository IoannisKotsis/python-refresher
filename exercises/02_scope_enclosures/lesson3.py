def make_counter():
    n = 0

    def inner():
        nonlocal n
        n += 1
        return n

    return inner


c = make_counter()
print(c(), c(), c())
