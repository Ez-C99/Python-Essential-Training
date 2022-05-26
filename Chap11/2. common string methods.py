#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

print('Hello, World.'.upper())  # Print in all upper case

print('Hello, World.'.lower())  # Print in all lower case

print('Hello, World.'.capitalize())    # Capitalise just first letter

print('Hello, World.'.title())  # Capitalise first letter of every word

print('Hello, World.'.swapcase())   # Swap cases of a everu letter

print('Hello, World.'.casefold) # Aggressive lowercase, removing all case distincations, even in unicode

# String is immutable ---> cannot be changed
## By using string methods on string, creates a whole new object with new ID, doesn't transform