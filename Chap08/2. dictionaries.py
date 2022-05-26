#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    animals = { 'kitten': 'meow', 'puppy': 'ruff!', 'lion': 'grrr',
        'giraffe': 'I am a giraffe!', 'dragon': 'rawr' }
    print_dict(animals)
    for k, v in animals.items():            # Same as print_dict function
        print(f'{k}: {v}')
    for k in animals.keys(): print(k)       # Print just the keys
    for v in animals.values(): print(v)     # Print just the values
    animals['monkey'] = 'haha'              # Add a new value
    print('found !' if 'monkey' in animals else 'no monkey')    # Search dictionary

def print_dict(o):
    for x in o: print(f'{x}: {o[x]}')

if __name__ == '__main__': main()




