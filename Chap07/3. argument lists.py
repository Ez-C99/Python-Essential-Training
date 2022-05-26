#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    kitten('meow', 'grrr', 'purr')

def kitten(*args):      # Take any number of arguments into function
    if len(args):       # Check if length>0 (0 is false)
        for s in args:
            print(s)
    else: print('Meow.')

if __name__ == '__main__': main()
