from tkinter.tix import Y_REGION


def make_generators_generator(g):
    """Generates all the "sub"-generators of the generator returned by
    the generator function g.

    >>> def every_m_ints_to(n, m):
    ...     i = 0
    ...     while (i <= n):
    ...         yield i
    ...         i += m
    ...
    >>> def every_3_ints_to_10():
    ...     for item in every_m_ints_to(10, 3):
    ...         yield item
    ...
    >>> for gen in make_generators_generator(every_3_ints_to_10):
    ...     print("Next Generator:")
    ...     for item in gen:
    ...         print(item)
    ...
    Next Generator:
    0
    Next Generator:
    0
    3
    Next Generator:
    0
    3
    6
    Next Generator:
    0
    3
    6
    9
    """
    "*** YOUR CODE HERE ***"
    # 这东西就自己想 感觉自己理解不透彻 但是看答案就能看到 好讨厌啊
    # 自己的做法有点抽象 但确实是自己搞出来了
    # def fun(l):
    #     yield from l

    # data = []
    # temp = g()
    # for x in temp:
    #     data.append(x)
    #     yield fun(data.copy())
    times = 1

    def fun():
        nonlocal times
        now_iter = iter(g())
        for _ in range(times):
            yield next(now_iter)
        times += 1
    temp = g
    l = list(iter(temp()))
    for _ in range(len(l)):
        yield fun()
