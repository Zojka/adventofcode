#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: zparteka
"""


def read(infile):
    with open(infile, 'r') as f:
        line = f.readline()
        rules = {}
        while line != "\n":
            rule = line.strip().split(':')
            key = rule[0]
            r1 = rule[1].split()[0].split("-")
            r2 = rule[1].split()[2].split("-")
            rules[key] = ((int(r1[0]), int(r1[1])), (int(r2[0]), int(r2[1])))
            line = f.readline()
        line = f.readline()
        ticket = [int(i) for i in f.readline().strip().split(",")]
        nearby = []
        f.readline()
        f.readline()
        while line:
            line = f.readline()
            if line != "":
                nearby.append([int(i) for i in line.strip().split(",")])
        return rules, ticket, nearby


def check_nearby(rules, nearby):
    rules = rules.values()
    rules = [i for sub in rules for i in sub]
    print(rules)
    wrong = 0
    for ticket in nearby:

        for number in ticket:
            flag = False
            for r in rules:
                if number in range(r[0], r[1] + 1):
                    flag = True
            if flag:
                continue
            else:
                wrong += number
                break
    return wrong


def remove_invalid(rules, nearby):
    rules = rules.values()
    rules = [i for sub in rules for i in sub]
    valid = []
    for ticket in nearby:
        tick = True
        for number in ticket:
            flag = False
            for r in rules:
                if number in range(r[0], r[1] + 1):
                    flag = True
            if flag:
                continue
            else:
                tick = False
                break
        if tick:
            valid.append(ticket)
    return valid


def find_positions(nearby, rules):
    transposed = list(map(list, zip(*nearby)))
    result = [0] * len(transposed)
    for row in range(len(transposed)):
        possible_rules = list(rules.keys())
        for number in transposed[row]:
            for name in rules.keys():
                rule = rules[name]
                if number not in range(rule[0][0], rule[0][1] + 1) and number not in range(rule[1][0], rule[1][1] + 1):
                    possible_rules.remove(name)
        result[row] = (possible_rules, row)
    result.sort(key=lambda t: len(t[0]))
    occured = [0] * len(result)
    for i in range(len(result)):
        for j in result[i][0]:
            if j not in occured:
                occured[result[i][1]] = j
    indexes = []
    for i in range(len(occured)):
        if occured[i].startswith("departure"):
            indexes.append(i)
    return indexes


def main():
    example = "input"
    rules, ticket, nearby = read(example)
    valid_nearby = remove_invalid(rules, nearby)
    indexes = find_positions(valid_nearby, rules)
    answer = 1
    for i in indexes:
        answer *= ticket[i]
        print(ticket[i])
    print(answer)
    print(ticket)


if __name__ == '__main__':
    main()
