#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

print('Hello, World.'.swapcase())   #Swap cases of all letters

print('Hello, World.'.format(42 * 7))   # Format calculation into string ---> works with variables too

class MyString(str):        # String variable in class
    def __str__(self):
        return self[::-1]   # Return reverse of any string

s = MyString('Hello World !')
print(s)