def composer(func=lambda x: x):
    def func_adder(g):
        return lambda x: g(x), func_adder
    return func, func_adder


def add_one(x): return x + 1
def mul_two(x): return x * 2


f, func_adder = composer()
f1, func_adder = func_adder(add_one)
f1(3)
f2, func_adder = func_adder(mul_two)
f2(3)  # should be 1 + (2*3) = 7
f3, func_adder = func_adder(add_one)
f3(3)  # should be 1 + (2 * (3 + 1)) = 9
