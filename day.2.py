#!/usr/bin/env python3

OPCODE_ADD = 1
OPCODE_MULT = 2
OPCODE_END = 99

input2 = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,2,19,6,23,2,13,23,27,1,9,27,31,2,31,9,35,1,6,35,39,2,10,39,43,1,5,43,47,1,5,47,51,2,51,6,55,2,10,55,59,1,59,9,63,2,13,63,67,1,10,67,71,1,71,5,75,1,75,6,79,1,10,79,83,1,5,83,87,1,5,87,91,2,91,6,95,2,6,95,99,2,10,99,103,1,103,5,107,1,2,107,111,1,6,111,0,99,2,14,0,0]

def intcode_run(ram):
    if (len(ram) < 1) :
        return ram

    current = 0

    while ram[current] != OPCODE_END:
        x, y, z = ram[current+1:current+4]
        if ram[current] == OPCODE_ADD:
            ram[z] = ram[x] + ram[y]
        elif ram[current] == OPCODE_MULT:
            ram[z] = ram[x] * ram[y]
        else:
            return [] # Error
        current += 4
    return ram

def execute():
    input2[1] = 12
    input2[2] = 2
    return intcode_run(input2)[0]

def verify(a, b):
    if (a == b):
        print("✓")
        return
    
    print (locals())

def test_cases():
    verify([], intcode_run([]))
    verify([3500,9,10,70,2,3,11,0,99,30,40,50], intcode_run([1,9,10,3,2,3,11,0,99,30,40,50]))
    verify([2,0,0,0,99], intcode_run([1,0,0,0,99]))
    verify([2,3,0,6,99], intcode_run([2,3,0,3,99]))
    verify([2,4,4,5,99,9801], intcode_run([2,4,4,5,99,0]))
    verify([30,1,1,4,2,5,6,0,99], intcode_run([1,1,1,4,99,5,6,0,99]))

if __name__ == "__main__":
    test_cases()
    print(execute())