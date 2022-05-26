#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = [ 1, 2, 3, 4, 5 ]           # List
x[0] = 23                       # List is mutable, values can be changed
for i in x:
    print('i is {}'.format(i))

y = ( 1, 2, 3, 4, 5 )           # Tuple
# y[0] = 23                     # Tuple immutable, values can't be changed
for j in y:
    print('j is {}'.format(j))

# Generally best to favour tuple over list unless you KNOW you need to
# change list elements

# Range function is immutable
z = range(10)   # Can expand to 3 parameters: (start, stop, step by)
# z = range (0, 10, 1)
for k in z:
    print(f'k is {k}')

# Dictionary = searchable sequence of key value pairs [mutable]
a = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
# 2 tuple can be returned with 2 loop variables and data.items()
for l, m in a.items():
    print(f'l: {l} has value m: {m}')