# -*- coding: utf-8 -*-
def triangles(max):
    # 求阶乘的函数
    def factorial(i):
        if i == 0:
            return 1
        elif i != 1:
            return i * factorial(i - 1)
        else:
            return i

    # 杨辉三角的通项公式：C(n-1, m-1)
    # 也就是 (n-1)! / [(m-1)! (n-m)!]
    def general(i, j):
        return int(factorial(i) / factorial(j) / factorial(i - j))

    # 第几行
    n = 0

    # Generator 本尊
    while n<max:
        yield(list([general(n, m) for m in range(n + 1)]))
        n += 1

# for l1 in triangles(3):
    print(l1)


def triangles_2(max):
    n=0
    result = [1]
    while n<max:
        yield result
        result = [1] + [result[x] + result[x + 1] for x in range(len(result) - 1)] + [1]
        n=n+1


for l1 in triangles_2(4):
    print(l1)