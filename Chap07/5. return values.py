#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


# Functions an procedures are the same, all functions return values

def main():
    x = kitten()        # Assign return value from function to variable
    print(type(x))

def kitten():
    print('Meow.')

if __name__ == '__main__': main()

# If there's no return value, variable is NoneType
# Otherwise type is that of whatever is returned, simple or complexS