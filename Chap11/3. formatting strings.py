#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 23
y = 69

print(' the number is {xx} {bb}'.format(xx = x, bb = y))

# Or use positional arguments

print(' the number is {1} {0}'.format(x, y))     # Positional arguments start from 1

z = x * y * 10000
print('the number is {:,}'.format(z))   # Colon and comma for thousands separation

print('the number is {:.3f}'.format(z/5.2))   # 3 decimal places fixed