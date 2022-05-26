#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


# kwarg = list argument using dictionary instead of tuple
## Function can have variable number of named arguments

def main():
    x = dict(Buffy = 'meow', Zilla = 'grr', Angel = 'rawr')
    kitten(**x)

def kitten(**kwargs):       # 2 asterisks instead of 1
    if len(kwargs):
        for k in kwargs:
            print('Kitten {} says {}'.format(k, kwargs[k]))
    else: print('Meow.')

if __name__ == '__main__': main()
