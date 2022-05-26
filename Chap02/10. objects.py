#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Duck:

    sound = 'Quack'             # Variables created inside class
    walking = 'Walks like a duck'

    def quack(self):            # First method in Class is always self
        print(self.sound)       ## Ref. to object when class used to instantiate

    def walk(self):
        print(self.walking)

def main():
    donald = Duck()         # Instantiate Donald from Duck class
    donald.quack()
    donald.walk()

if __name__ == '__main__': main()
