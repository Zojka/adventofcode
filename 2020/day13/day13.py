#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: zparteka
"""
import numpy as np

def read_notes(infile):
    with open(infile, 'r') as f:
        timestamp = int(f.readline().strip())
        bus = f.readline().strip().split(',')
        bus[:] = (int(value) for value in bus if value != 'x')
    return timestamp, bus

def find_bus(timestamp, busses):
    departures = []
    for i in busses:
        departures.append(timestamp - (timestamp%i) + i)
    return (min(departures)- timestamp) * busses[np.argmin(departures)]

def read_notes_part2(infile):
    with open(infile, 'r') as f:
        timestamp = int(f.readline().strip())
        bus = f.readline().strip().split(',')
    return bus

def part2(busses):
    timestamp = int(busses[0])
    indexes = []
    multiplied = []
    for i in range(len(busses)):
        for j in range(len(busses)):
            N = busses[i] * busses[j]

def main():
    # timestamp, busses = read_notes("input13")
    # print(find_bus(timestamp, busses))
    busses = read_notes_part2("input13")
    print(part2(busses))
if __name__ == '__main__':
       main()