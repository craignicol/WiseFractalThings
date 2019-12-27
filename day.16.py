#!/usr/bin/env python3

import numpy as np # Let's do matrix math

input_txt = "59740570066545297251154825435366340213217767560317431249230856126186684853914890740372813900333546650470120212696679073532070321905251098818938842748495771795700430939051767095353191994848143745556802800558539768000823464027739836197374419471170658410058272015907933865039230664448382679990256536462904281204159189130560932257840180904440715926277456416159792346144565015659158009309198333360851441615766440174908079262585930515201551023564548297813812053697661866316093326224437533276374827798775284521047531812721015476676752881281681617831848489744836944748112121951295833143568224473778646284752636203058705797036682752546769318376384677548240590"

def execute():
    return fft_f(input_txt, 100)

def verify(expected, actual):
    if (expected == actual):
        print("✓")
        return
    else:
        print (locals())

base_pattern = [0, 1, 0, -1]

mult_f = {-1: '-', 0: '.', +1: '+'}

def one_digit(inp, pos):
    pos_pattern = [0] * (pos+1) + [1] * (pos+1) + [0] * (pos+1) + [-1] * (pos+1)
    mult_pattern = (pos_pattern * ((len(inp) // len(pos_pattern)+1)))[1:len(inp)+1]
    print('*', ''.join([mult_f[m] for m in mult_pattern]))
    return abs(sum([a*b for a,b in zip(inp, mult_pattern)])) % 10

def one_phase(inp):
    if type(inp) == type(""):
        inp = [int(i) for i in inp]
    return [one_digit(inp, p) for p in range(len(inp))]

def one_phase_f(inp):
    return ''.join([str(i) for i in one_phase(inp)[:8]])

def fft(inp, phases):
    for p in range(phases):
        inp = one_phase(inp)
    return inp

def fft_f(inp, phases):
    return ''.join([str(i) for i in fft(inp,phases)[:]])

def fft_fast(inp, phases):
    out = [(int(i)+5) % 10 for i in inp[:-4]] + [int(i) for i in inp[-4:]]
    return out

def fft_fast_f(inp, phases):
    return ''.join([str(i) for i in fft_fast(inp,phases)[:]])

def test_cases():
    print("--- one_phase")
    verify("48226158", one_phase_f("12345678"))
    verify("34040438", one_phase_f("48226158"))
    verify("03415518", one_phase_f("34040438"))
    verify("01029498", one_phase_f("03415518"))

    print("--- fft")
    verify("24176176", fft_f("80871224585914546619083218645595", 100))
    verify("73745418", fft_f("19617804207202209144916044189917", 100))
    verify("52432133", fft_f("69317163492948606335995924319873", 100))

    print("--- 10k fft")
    verify(fft_f("80871224585914546619083218645595", 100), fft_fast_f("80871224585914546619083218645595", 100))
    verify(fft_f("19617804207202209144916044189917", 100), fft_fast_f("19617804207202209144916044189917", 100))
    verify(fft_f("69317163492948606335995924319873", 100), fft_fast_f("69317163492948606335995924319873", 100))


"""
{'expected': '24176176480919046114038763195595',              'actual': '35326779030469091164538763195595'}
{'expected': '73745418557257259149466599639917', 
   'actual': '64162359752757754699461599639917'}
{'expected': '52432133292998606880495974869873',
   'actual': '14862618947493151880440479869873'}"""

if __name__ == "__main__":
    test_cases()
    # print(execute())