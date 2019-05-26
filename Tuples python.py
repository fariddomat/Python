t = (("ab", 3), ("ab", 5), ("x", 6))
def s(t):
    st = ()
    num = ()
    for i in t:
        if i[0] not in st:
            st = st + (i[0],)
        num = num + (i[1],)
    print(st)
    print(num)
s(t)
