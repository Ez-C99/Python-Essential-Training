#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    game = [ 'Rock', 'Paper', 'Scissors', 'Lizard', 'Spock' ]
    print(game[1:3])        # Print non-inclusive of last index (Paper and Scissors)
    print(game[1:5:2])      # Print range with every second step (Paper and Lizard)
    i = game.index('Paper') # Return index of data value
    game.append('Computer') # Add item to list
    game.insert(5, 'First') # Insert item as specific data index
    game.remove('Computer') # Remove item from the list
    game.pop()              # Remove item from end of list (add index in brackets for specific)
    del game[4]             # Remove item by index (add index range to remove by slice)
    print(len(game))
    
    print_list(game)

def print_list(o):
    for i in o: print(i, end=' ', flush=True)
    print()

if __name__ == '__main__': main()

