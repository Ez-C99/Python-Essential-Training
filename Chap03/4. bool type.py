#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# Logical test of a NoneType value returns false

x = None
print('x is {}'.format(x))
print(type(x))

if x:
    print('True')
else:
    print('False')


# Same with any numeric zero
## Any non-zero number returns True
y = 0
print('y is {}'.format(y))
print(type(y))

if y:
    print('True')
else:
    print('False')


# Same with any empty string

z = ""
print('z is {}'.format(z))
print(type(z))

if z:
    print('True')
else:
    print('False')
