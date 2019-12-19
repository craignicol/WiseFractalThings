#!/usr/bin/env python3

import itertools

def execute():
    with open('input.8.txt') as inp:
        lines = inp.readlines()
    pixels = [l.strip() for l in lines if len(l.strip()) > 0]
    print(draw(pixels[0], 25, 6).replace('0',' '))
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

def collapse_layer(total, current):
    for x in range(len(current)):
        if current[x] == '2': # transparent
            pass
        else:
            total[x] = current[x]
    return total

def draw(pixels, width, height):
    # Split into layers, each width*height big
    lsize = width*height
    layers = [list(pixels[x*lsize:(x+1)*lsize]) for x in range(len(pixels)//lsize)]

    # Collapse layers
    img = itertools.accumulate(layers[::-1], collapse_layer)

    # Render
    final_p = list(img)[-1]
    return '\n'.join(''.join(final_p[r*width:(r+1)*width]) for r in range(height))

def test_cases():
    verify(1, checksum("123456789012", 3, 2))
    verify(['0', '1'], collapse_layer(['1','1'], ['0','2']))
    verify("01\n10", draw("0222112222120000", 2, 2))

if __name__ == "__main__":
    test_cases()
    print(execute())