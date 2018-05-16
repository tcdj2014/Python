# -*- coding: utf-8 -*-
def fact(n):
    if n == 1 or n == 0:
        return 1
    return n * fact(n - 1)


# print(fact(200))


# 尾递归优化
def fact2(n):
    if n == 0:
        return 1
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


print(fact(2))
print(fact2(200))


def hannuta(n, a, b, c):
    if (n == 1):
        print(a, "-->", c)
    else:
        hannuta(n - 1, a, c, b)
        hannuta(1, a, b, c)
        hannuta(n - 1, b, a, c)


hannuta(3,"A","B","C");
