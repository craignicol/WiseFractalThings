#!/usr/bin/env python3

from collections import defaultdict
from math import ceil

def execute():
    with open('day.n.py') as inp:
        lines = inp.readlines()
    return len([l.strip() for l in lines if len(l.strip()) > 0])

def verify(expected, actual):
    if (expected == actual):
        print("✓")
        return
    else:
        print (locals())

reaction0 = """5 ORE => 1 FUEL"""

reaction1 = """10 ORE => 10 A
1 ORE => 1 B
7 A, 1 B => 1 C
7 A, 1 C => 1 D
7 A, 1 D => 1 E
7 A, 1 E => 1 FUEL"""

reaction2 = """9 ORE => 2 A
8 ORE => 3 B
7 ORE => 5 C
3 A, 4 B => 1 AB
5 B, 7 C => 1 BC
4 C, 1 A => 1 CA
2 AB, 3 BC, 4 CA => 1 FUEL"""

def test_cases():
    verify(5, ore_for_fuel(reaction0))
    verify(31, ore_for_fuel(reaction1))
    verify(165, ore_for_fuel(reaction2))

def split_units(un):
    amount, unit = un.split()
    return (int(amount), unit)

def format_reaction(reaction):
    source, target = reaction
    target = split_units(target)
    source = [split_units(s) for s in source.split(', ')]
    return (target[1], (target[0], source))

def ore_for_fuel(rules):
    reactions = [react.split(' => ') for react in rules.splitlines(keepends = False)]
    components = dict([format_reaction(r) for r in reactions])
    composition = defaultdict(int)
    composition['FUEL'] = 1
    composition['ORE'] = 0
    while len(composition) > 1:
        k = list(composition.keys())
        atom = k[-1] if k[-1] != 'ORE' else k[-2]
        amount = composition.pop(atom)
        required = components[atom]
        multiplier = ceil(amount / required[0])
        ingredients = required[1]
        for (howmuch, unit) in ingredients:
            composition[unit] += howmuch * multiplier
#        print (required, multiplier, composition)

    return composition['ORE']

if __name__ == "__main__":
    test_cases()
    print(execute())