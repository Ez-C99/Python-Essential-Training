#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# Multiply int by float and get a float

# Divide int by int and (if it's decimal) get a float
## Double divide (//) gives int answer without remainder

# Float numbers don't work well with money since they sacrifice accuracy
# for precision

from decimal import *       # From decimal import everything
                            #Allows accurate decimal work

a = Decimal('.10')          # 2 decimal places
b = Decimal('.30')

x = a + a + a - b

print('x is {}'.format(x))
print(type(x))
