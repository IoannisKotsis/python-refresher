# 2.2
funcs = []
for i in range(3):

    def f(z=i):

        return z * 10

    funcs.append(f)

i = 100
print([g() for g in funcs])
