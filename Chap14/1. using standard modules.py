#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import sys
import os
import random
import datetime

def main():
    v = sys.version_info
    print('Python version {}.{}.{}'.format(*v))
    p = sys.platform
    print(p)

    o = os.name
    print(o)
    e = os.getenv
    print(e)
    c = os.getcwd
    print(c)

    x = random.randint(1,1000)
    print(x)
    y = list(range(26))
    print(y)
    random.shuffle(y)
    print(y)

    now = datetime.date.today()
    print(now)

if __name__ == '__main__': main()
