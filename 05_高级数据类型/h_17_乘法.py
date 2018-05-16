# -*- coding: utf-8 -*-
def product(x, *y):
    p=1;
    for temp in y:
        p*=temp
    return  x*p

print(product(8,8,9))