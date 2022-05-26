#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

secret = 'swordfish'
pw = ''
try_count = 5

while (pw != secret) and (try_count != 0):
    print(f'You have {try_count} attemps left')
    pw = input("What's the secret word? ")
    try_count-=1
