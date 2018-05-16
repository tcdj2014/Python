def say_hello():
    """打招呼"""
    print("hello 1")
    print("hello 2")
    print("hello 3")


def m_table():
    i = 1
    j = 1
    while i <= 9:
        while j <= i:
            print("%d*%d=%d" % (i, j, i * j), end="\t")
            j += 1
        print()
        j = 1
        i += 1
