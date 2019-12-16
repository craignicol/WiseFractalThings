#!/usr/bin/env python3

def execute():
    with open('input.6.txt') as inp:
        lines = inp.readlines()
    orbits = [l.strip() for l in lines]
    return count_orbits(orbits), shortest_route(orbits)

def verify(expected, actual):
    if (expected == actual):
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

# Need to find lowest common orbit
def shortest_route(input1):
    START = "YOU"
    END = "SAN"
    cleansed = [o.split(")") for o in input1]
    planets = plan_routes(cleansed)
    return len(set(planets[START]) ^ set(planets[END]))

def plan_routes(input1):
    planetset = [(x[1], []) for x in input1] + [(ROOT_NODE, [])]
    planets = dict(planetset)
    next_planets = [x for x in input1 if x[0] == ROOT_NODE]
    while len(next_planets) > 0:
        for ip in next_planets:
            planets[ip[1]] = planets[ip[0]] + [ip[0]]
        ips = [p[1] for p in next_planets]
        next_planets = [x for x in input1 if x[0] in ips]
    
    return planets

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