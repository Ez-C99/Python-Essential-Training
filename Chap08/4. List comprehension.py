#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    seq = range(11)
    seq2 = [x*2 for x in seq]       # New list of all elements doubled
    print_list(seq)
    print_list(seq2)
    seq3 = [x for x in seq if x%3 != 0] # New list of everything not divisible by 3
    print_list(seq3)
    seq4 = [(x, x**2) for x in seq]     # List of tuples
    print(seq4)
    seq5 = {x for x in 'superduper' if x not in 'pd'}   # Set from string without p or d
    print(seq5)

def print_list(o):
    for x in o: print(x, end = ' ')
    print()

if __name__ == '__main__': main()
