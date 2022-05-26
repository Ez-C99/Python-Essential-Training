#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Duck:
    sound = 'Quack quack.'              # Attributes
    movement = 'Walks like a duck.'     

    def quack(self):                    # Methods
        print(self.sound)

    def move(self):                 # Use self so people reading code know what you mean
        print(self.movement)        ## self = reference to any object created from the class

def main():
    donald = Duck()             # Instantiate class (object)
    donald.quack()              ## perform class methods
    donald.move()

if __name__ == '__main__': main()
