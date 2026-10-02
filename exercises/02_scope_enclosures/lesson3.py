def make_counter(n):
    def inner():
        return n + 1

    print(inner())


make_counter(3)
