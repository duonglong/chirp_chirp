def tamvm(n, c):
    r = ''
    while n > 0:
        print n
        if n & 1:
            r += c
            n >>= 1
        if n:
            c += c
    return r
tamvm(100, "c")
