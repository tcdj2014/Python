# -*- coding: utf-8 -*-
def fib_1(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

# 创建一个generator []->(),print->yield
def fib_2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

print(fib_1(20))
print(fib_2(20))
for g in fib_2(20):
    print(g)