#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# Copy binary file

def main():
    infile = open('Chap12/berlin.jpg', 'rb')    # rb = read binary
    outfile = open('berlin-copy.jpg', 'wb')     # wb = read
    while True:
        buf = infile.read(10240)                # pick safe buffer size (10k bytes) --> don't know data size
        if buf:
            outfile.write(buf)
            print('.', end='', flush=True)
        else: break                             # break if buffer empty
    outfile.close()                             # close file to prevent buffering data loss
    print('\ndone.')

if __name__ == '__main__': main()
