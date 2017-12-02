#!/usr/bin/python

from decimal import *

def checksum(line):
    checksum = 0
    entries = [int(i.strip()) for i in line.split(';') if i.strip()]

    for idx1, i in enumerate(entries):
        for idx2, j in enumerate(entries):
            if idx1 != idx2:
                x = Decimal(j) / Decimal(i)
                if x % 1 == 0:
                    checksum += x
    return checksum

for f in ('input_test02.csv', 'input.csv'):
    answer = 0
    with open(f) as file:
        lines = file.readlines()

    for line in lines:
        answer += checksum(line)

    print("answer for {}: {}".format(f, answer))
