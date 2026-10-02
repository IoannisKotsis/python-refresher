# 2.2 (alternative)
def make_f(n):
    def adding():
        return n * 10

    return adding


funcs = []
for i in range(3):
    funcs.append(make_f(i))

i = 100
print([g() for g in funcs])
