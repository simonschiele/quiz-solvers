#!/usr/bin/python

def checksum(line):
    entries = [int(i.strip()) for i in line.split(';') if i.strip()]
    smallest = min(entries)
    biggest = max(entries)
    return biggest - smallest

for f in ('input_test01.csv', 'input.csv'):
    answer = 0
    with open(f) as file:
        lines = file.readlines()

    for line in lines:
        answer += checksum(line)

    print("answer for {}: {}".format(f, answer))
