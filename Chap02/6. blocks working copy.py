#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 42
y = 73

if x < y:
    end_message = 'end'
    print('x < y: x is {} and y is {}'.format(x, y))
    print('line 1')
    print('line 2')
print('line 4')         ## un-indenting lines brings it outside if statement scope

print(end_message)      ## blockd don't define variable scope
