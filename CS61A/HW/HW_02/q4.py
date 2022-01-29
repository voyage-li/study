# 刚开始不是很理解什么意思

def zero(f):
    return lambda x: x


def successor(n):  # 参数是函数 返回的同样是函数
    return lambda f: lambda x: f(n(f)(x))


def one(f):  # 参数是一个函数
    """Church numeral 1: same as successor(zero)"""
    "*** YOUR CODE HERE ***"
    return lambda x: f(x)


def two(f):
    """Church numeral 2: same as successor(successor(zero))"""
    "*** YOUR CODE HERE ***"
    return lambda x: f(f(x))


three = successor(two)


def church_to_int(n):
    """Convert the Church numeral n to a Python integer.
    >>> church_to_int(zero)
    0
    >>> church_to_int(one)
    1
    >>> church_to_int(two)
    2
    >>> church_to_int(three)
    3
    """
    "*** YOUR CODE HERE ***"
    return n(lambda x: x + 1)(0)  # 把这个函数变成 +1 这样几就是调用多少个 +1


def add_church(m, n):
    """Return the Church numeral for m + n, for Church numerals m and n.
    >>> church_to_int(add_church(two, three))
    5
    """
    "*** YOUR CODE HERE ***"
    return lambda f: lambda x: m(f)(n(f)(x))


def mul_church(m, n):
    """Return the Church numeral for m * n, for Church numerals m and n.
    >>> four = successor(three)
    >>> church_to_int(mul_church(two, three))
    6
    >>> church_to_int(mul_church(three, four))
    12
    """
    "*** YOUR CODE HERE ***"
    return lambda f: n(m(f))  # m(f)运算 n次


def pow_church(m, n):
    """Return the Church numeral m ** n, for Church numerals m and n.
    >>> church_to_int(pow_church(two, three))
    8
    >>> church_to_int(pow_church(three, two))
    9
    """
    "*** YOUR CODE HERE ***"
    return lambda f: (n(m))(f)  # 运算 m^n 次
