#!/usr/bin/env python3

def execute():
    with open('input.8.txt') as inp:
        lines = inp.readlines()
    pixels = [l.strip() for l in lines if len(l.strip()) > 0]
    return checksum(pixels[0], 25, 6)

def verify(expected, actual):
    if (expected == actual):
        print("✓")
        return
    else:
        print (locals())

def checksum(pixels, width, height):
    # Split into layers, each width*height big
    lsize = width*height
    layers = [list(pixels[x*lsize:(x+1)*lsize]) for x in range(len(pixels)//lsize)]
    # Find layer with fewest zeroes
    chosen_layer = sorted(layers, key=lambda l : l.count('0'))[0]
    # For this layer, multiply count of 1s * 2s
    return chosen_layer.count('1') * chosen_layer.count('2')

def test_cases():
    verify(1, checksum("123456789012", 3, 2))

if __name__ == "__main__":
    test_cases()
    print(execute())