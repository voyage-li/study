def add_chars(w1, w2):
    l1 = len(w1)
    l2 = len(w2)
    ans = ''

    def fun(i, j, now):
        if i >= l1 and j >= l2:
            return now
        elif i >= l1 and j < l2:
            now += w2[j]
            return fun(i, j+1, now)
        else:
            if w1[i] == w2[j]:
                return fun(i+1, j+1, now)
            else:
                now += w2[j]
                return fun(i, j+1, now)

    return fun(0, 0, ans)


print(add_chars("owl", "howl"))
