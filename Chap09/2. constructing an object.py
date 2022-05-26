#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Animal:
    def __init__(self, **kwargs):      # init = constructor/initialiser class function ---> pass arguments (1st is always self)
        self._type = kwargs['type']                       ## Initialise object variabe
        self._name = kwargs['name']     # kwargs used so variable order doesn't need to be specified
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'rawr'  # kwargs allow default value

    def type(self):
        return self._type                       # Getters/accessors to return value of variables

    def name(self):
        return self._name

    def sound(self):
        return self._sound

def print_animal(o):
    if not isinstance(o, Animal):
        raise TypeError('print_animal(): requires an Animal')
    print('The {} is named "{}" and says "{}".'.format(o.type(), o.name(), o.sound()))


def main():
    a0 = Animal(type='kitten', name='fluffy', sound='rwar')
    a1 = Animal(type='duck', name='donald', sound='quack')
    print_animal(a0)
    print_animal(a1)
    print_animal(Animal(type='velociraptor', name='veronica', sound='hello'))
    #print_animal(Animal())     With all kwarg defaults set, this prints an object with them

if __name__ == '__main__': main()
