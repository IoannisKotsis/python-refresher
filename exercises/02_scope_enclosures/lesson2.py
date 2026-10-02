# 2.2 (alternative)
funcs = []


def f():
    def adding():
        for i in range(3):
            funcs.append(i * 10)

    return funcs


f()
