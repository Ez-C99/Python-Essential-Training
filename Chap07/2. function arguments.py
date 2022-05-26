#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    kitten(5,6,7)

def kitten(a,b,c=0):      # Function can take multiple arguments
    print('Meow.')        ## set to have default value for if value isn't passed
    print(a,b,c)          ## Arguments with defaults have to be AFTER those without defaults

if __name__ == '__main__': main()

# Integer is immutable so when you assign new value, you're assigning new object to the name
# Original integer isn't changing

