#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# Decorator = function type that returns a wrapper function

# Everything in Python = object ---> function =  type of object
# Functons define scope ---> main cannot call function inside another
## First function is the 'wrapper' for the second

import time

def elapsed_time(f):
    def wrapper():
        t1 = time.time()
        f()
        t2 = time.time()
        print(f'Elapsed time: {(t2 - t1) * 1000} ms')
    return wrapper


@elapsed_time       # decorator function
def big_sum():      # function passed as argument to decorator
    num_list = []
    for num in (range(0, 10000)):
        num_list.append(num)
    print(f'Big sum: {sum(num_list)}')

def main():
    big_sum()

if __name__ == '__main__': main()
