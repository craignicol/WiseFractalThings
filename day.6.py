#!/usr/bin/env python3

def execute():
    with open('input.6.txt') as inp:
        lines = inp.readlines()
    orbits = [l.strip() for l in lines]
    return count_orbits(orbits), shortest_route(orbits)

def verify(a, b):
    if (a == b):
        print("✓")
        return
    
    print (locals())

ROOT_NODE = "COM"

input1 = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L"""

input2 = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN"""

def shortest_route(input1):
    START = "YOU"
    END = "SAN"
    cleansed = [o.split(")") for o in input1]
    planets = measure_routes(cleansed)
    return planets[START], planets[END]

def measure_routes(input1):
    planets = dict({(x[1], 0) for x in input1})
    next_planets = [x[1] for x in input1 if x[0] == ROOT_NODE]
    distance = 1
    while len(next_planets) > 0:
        for ip in next_planets:
            planets[ip] = distance
        distance += 1
        next_planets = [x[1] for x in input1 if x[0] in next_planets]
    
    return planets

def count_routes(input1):
    planets = measure_routes(input1)
    return sum(planets.values())

def count_orbits(input1):
    cleansed = [o.split(")") for o in input1]
    return count_routes(cleansed)

def test_cases():
    verify(1, count_orbits(["COM)B"]))
    verify(42, count_orbits(input1.splitlines()))
    verify(4, shortest_route(input2.splitlines()))

if __name__ == "__main__":
    test_cases()
    print(execute())