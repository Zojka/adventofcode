#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: zparteka
"""


def read_data(infile):
    masks = {}
    with open(infile, 'r') as f:
        data = f.readlines()
        for i in range(len(data)):
            if data[i].strip().startswith("mask"):
                mask = data[i].strip()[7:]
                counter = i + 1
                masks[mask] = []
                while data[counter].startswith("mem"):
                    line = data[counter].strip().split(' = ')
                    masks[mask].append((int(line[0][4:-1]), int(line[1])))
                    if counter == len(data) - 1:
                        return masks
                    else:
                        counter += 1


def masking(masks):
    numbers = {}
    for i in masks.keys():
        for j in masks[i]:
            mask = format(j[1], "036b")
            for n in range(len(mask)):
                if i[n] != "X" and mask[n] != i[n]:
                    mask = mask[:n] + i[n] + mask[n + 1:]
            numbers[j[0]] = int(mask, 2)
    return sum(list(numbers.values()))


def part2(masks):
    numbers = {}
    number_counter = 0
    for i in masks.keys():
        print(i)
        for j in masks[i]:
            print(j[0])
            mask = format(j[0], "036b")
            counter = 0
            for n in range(len(mask)):
                if i[n] == '0':
                    continue
                elif i[n] == '1':
                    mask = mask[:n] + '1' + mask[n + 1:]
                if i[n] == 'X':
                    counter += 1
                    mask = mask[:n] + 'X' + mask[n + 1:]
            arr = [None] * counter
            ready = []
            generate_binary(counter, arr, 0, ready)
            for variation in ready:

                print(variation)
                counter = 0
                fmask = mask
                for k in range(len(fmask)):
                    if fmask[k] == "X":
                        fmask = fmask[:k] + str(variation[counter]) + fmask[k + 1:]
                        counter += 1
                numbers[int(fmask, 2)] = j[1]
                number_counter += 1
    print(number_counter)
    print(len(numbers.keys()))
    return sum(list(numbers.values()))


def generate_binary(n, arr, i, ready):
    barr = arr[:]
    if i == n:
        ready.append(barr)
        return
    barr[i] = 0
    generate_binary(n, barr, i + 1, ready)
    barr[i] = 1
    generate_binary(n, barr, i + 1, ready)


def main():
    masks = read_data("input_day14")
    print(part2(masks))


if __name__ == '__main__':
    main()
