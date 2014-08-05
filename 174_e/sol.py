"""
http://www.reddit.com/r/dailyprogrammer/comments/2cld8m/8042014_challenge_174_easy_thuemorse_sequences/
"""

import argparse


def increment_num_based(input_num, len):
    print "input is ", bin(input)
    print bin(input << len(str(bin(input))))
    print bin(~input)
    return input << len(str(bin(input))) - (~input)


def thue_morse_num_based(entry):
    print "Calculating thue_morse for %s" % entry
    calculated = 0
    if entry > 0:
        for i in range(1, entry+1):
            calculated = increment(calculated)
    return calculated


def flip(digit):
    if digit == '0':
        return '1'
    else:
        return '0'


def increment(in_str):
    return in_str + "".join([flip(x) for x in in_str])


def thue_morse_str_based(entry):
    sequence = "0"
    if entry > 0:
        for i in range(1, entry+1):
            sequence = increment(sequence)
    return sequence

for i in range(6):
    print thue_morse_str_based(i)
i = thue_morse_str_based(25)
print len(i)
