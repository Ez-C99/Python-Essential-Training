#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def function(n = 1):        # function given default value ( 1 ) so if n isn't passed a value, it uses that
    print(n)
    return n * 2

x = function(47)            # result of function assigned to x
print(x)
