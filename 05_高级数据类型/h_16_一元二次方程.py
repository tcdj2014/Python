# -*- coding: utf-8 -*-
import math
def quadratic(a, b, c):
    if not isinstance(a,(int)):
        raise TypeError("a不是整数")
    elif not isinstance(b,(int)):
        raise TypeError("b不是整数")
    elif not isinstance(c,(int)):
        raise TypeError("c不是整数")

    if a==0:
        raise TypeError("a不能为0")

    delta_squared = b ** 2 - 4 * a * c

    if delta_squared<0:
        return None
    else:
        delta=math.sqrt(delta_squared)
        x1=(-b+delta)/2/a
        x2=(-b-delta)/2/a
        return x1,x2



for result in quadratic(1,-2,1):
    print(result,end=" ")