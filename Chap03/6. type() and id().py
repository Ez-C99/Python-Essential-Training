#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = (1, 'two', 3.0, [4, 'four'], 5)
print('x is {}'.format(x))
print(type(x[1]))           
# You can inspect any element in structure and it gives specific type

y = (1, 'two', 3.0, [4, 'four'], 5)
print('y is {}'.format(y))
print(type(id(y)))          # id() returns unique identifier for an object

## Compare objects

if x[0] is y[0]:        # This would be True
    print('Yep')
else:
    print('Nope')

if x is y:              # This would be False
    print('Yep')
else:
    print('Nope')

## isinstance allows you to test type of structure
#whereas type() jsut prints type
if isinstance(x, tuple):
    print('Yep a tuple')
else:
    print('nope not a tuple')
