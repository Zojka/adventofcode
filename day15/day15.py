#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: zparteka
"""
starting_numbers = [0,3,6]

def play(starting_numbers, end_turn=30000000):
    numbers = {}
    for i in range(len(starting_numbers)):
        numbers[starting_numbers[i]] = i + 1
        last = starting_numbers[i]
    turn = i + 2
    last = 0
    while turn <= end_turn:
        if last in numbers.keys():
            new_last = last
            last = turn - numbers[new_last]
            numbers[new_last] = turn
            turn += 1
        else:
            new_last = last
            last = 0
            numbers[new_last] = turn
            turn += 1

    return new_last

def main():
    final = [16,11,15,0,1,7]
    print(play(final))
if __name__ == "__main__":
    main()