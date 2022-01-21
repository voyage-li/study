def hailstone(x):
    """Print the hailstone sequence starting at x and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    fre = 1
    while x > 1:
        print(x)
        fre += 1
        if x % 2 == 0:
            x = x//2
        else:
            x = 3*x+1
    print(1)
    return fre


a = hailstone(10)
print(a)
