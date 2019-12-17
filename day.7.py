#!/usr/bin/env python3

import itertools

OPCODE_ADD = 1
OPCODE_MULT = 2
OPCODE_READ = 3
OPCODE_WRITE = 4
OPCODE_JUMPIFTRUE = 5
OPCODE_JUMPIFFALSE = 6
OPCODE_LESSTHAN = 7
OPCODE_EQUALS = 8
OPCODE_END = 99

opcode_name    = [None, "+", "*", "Read", "Write", "£True", "£False", "<", "="]
argument_count = [0, 3, 3, 1, 1, 2, 2, 3, 3]

input2 = [3,8,1001,8,10,8,105,1,0,0,21,34,47,72,93,110,191,272,353,434,99999,3,9,102,3,9,9,1001,9,3,9,4,9,99,3,9,102,4,9,9,1001,9,4,9,4,9,99,3,9,101,3,9,9,1002,9,3,9,1001,9,2,9,1002,9,2,9,101,4,9,9,4,9,99,3,9,1002,9,3,9,101,5,9,9,102,4,9,9,1001,9,4,9,4,9,99,3,9,101,3,9,9,102,4,9,9,1001,9,3,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,99]

debug = False

def unpack_arguments(ram, current):
        next_opcode = ram[current] % 100

        if current + argument_count[next_opcode] >= len(ram):
            raise ValueError("Cannot unpack {} arguments from: {}".format( argument_count[next_opcode], ram[current:]))

        if argument_count[next_opcode] == 3:
            x, y, z = ram[current+1:current+4]
        elif argument_count[next_opcode] == 2:
            x, y = ram[current+1:current+3]
            z = None
        elif argument_count[next_opcode] == 1:
            x = ram[current+1]
            y, z = None, None
        else:
            x, y, z = None, None, None

        xm = (ram[current] // 100) % 10 == 1
        ym = (ram[current] // 1000) % 10 == 1
        zm = (ram[current] // 10000) % 10 == 1

        xval = x if xm == 1 or x is None else ram[x]
        yval = y if ym == 1 or y is None else ram[y]
        zval = z if zm == 1 or z is None else ram[z]

        if debug:
            print(current, ":", opcode_name[next_opcode], "; {} => {} ; {} => {} ; {} => {}".format(x, xval, y, yval, z, zval))

        return next_opcode, x, xval, y, yval, z, zval

def intcode_run(ram, inputs=[]):
    if len(ram) < 1:
        return ram

    current = 0
    next_input = 0
    output = []

    while ram[current] % 100 != OPCODE_END:
        next_opcode, x, xval, y, yval, z, zval = unpack_arguments(ram, current)

        if next_opcode == OPCODE_ADD:
            ram[z] = xval + yval
        elif next_opcode == OPCODE_MULT:
            ram[z] = xval * yval
        elif next_opcode == OPCODE_READ:
            ram[x] = inputs[next_input]
            next_input += 1
        elif next_opcode == OPCODE_WRITE:
            output.append(xval)
        elif next_opcode == OPCODE_JUMPIFTRUE:
            current = yval if xval != 0 else current + 3
            continue
        elif next_opcode == OPCODE_JUMPIFFALSE:
            current = yval if xval == 0 else current + 3
            continue
        elif next_opcode == OPCODE_LESSTHAN:
            ram[z] = 1 if xval < yval else 0
        elif next_opcode == OPCODE_EQUALS:
            ram[z] = 1 if xval == yval else 0
        else:
            return [] # Error

        if next_opcode <= len(argument_count):
            current += argument_count[next_opcode] + 1        
 
    return output

def intcode_amp(ram, seq):
    output = [0]
    for s in seq:
        output = intcode_run(ram, [s, output[0]])
    return output, seq

def intcode_max(ram):
    max_boost = 0
    max_p = []
    for p in itertools.permutations(range(5)):
        output, seq = intcode_amp(ram, p)
        if output[0] > max_boost:
            max_boost = output[0]
            max_p = p
    return max_boost, max_p

def execute():
    return intcode_max(input2)

def verify(a, b):
    if (a == b):
        print("✓")
        return
    
    print (locals())

def test_cases():
    verify([], intcode_run([]))

    verify(([43210], [4,3,2,1,0]), intcode_amp([3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0], [4, 3, 2, 1, 0]))

    verify((43210, (4,3,2,1,0)), intcode_max([3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]))
    verify((54321, (0,1,2,3,4)), intcode_max([3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]))
    verify((65210, (1,0,4,3,2)), intcode_max([3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]))


if __name__ == "__main__":
    test_cases()
    print(execute())