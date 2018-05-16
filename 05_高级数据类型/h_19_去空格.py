# -*- coding: utf-8 -*-
def trim(s):
    while s[:1] == ' ' or s[-1:] == ' ':
        if s[:1] == ' ':
            s = s[1:]
        else:
            s = s[:-1]
    return s

s="  hello "
print(trim(s))

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)