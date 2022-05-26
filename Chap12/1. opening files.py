#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    f = open('Chap12/lines.txt')        # Open file and store in object variable
    for line in f:                      # for loop to print each file
        print(line.rstrip())

if __name__ == '__main__': main()


#   open('file name', 'r')  =   read mode (default)
#   open('file name', 'w')  =   write mode
#   open('file name', 'a')  =   append mode