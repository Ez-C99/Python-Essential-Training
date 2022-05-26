#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


## Triple quotes ---> multi-line string

x = 'seven'.upper()      # Strings = objects ---> can run methods on them

y = 'seven {} {}'.format(8,9)   # positional into strings to variable
                                ## Can be arguments instead of values
# OR
## Use f string to enter identifiers in format
m = 1
n = 2
y1 = f'seven {m} {n}'   # f string are Python 3.6 and later

z = 'seven {1} {0}'.format(8,9)   # can be specified to swap positions

a = 'seven "{1:<9}" "{0:>9}"'.format(8,9) # add no. of spaces either side of value
# Adding 0s before no. of spaces adds leading 0s

print('x is {}'.format(x))
print(type(x))
