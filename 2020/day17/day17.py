#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: zparteka
"""
import numpy as np


def read(inpt):
    with open(inpt, 'r') as f:
        data = []
        line = f.readline()
        while line:
            data.append(list(line.strip()))
            line = f.readline()
        return [data]


def create_universe(data, multi=15):
    z = 1
    x = len(data[0])
    y = len(data[0][0])
    univ = np.empty((z * multi, x * multi, y * multi), dtype=str)
    for i in range(x):
        ax = x * multi // 2 + i - 1
        for j in range(y):
            az = multi // 2
            ay = y * multi // 2 + j - 1
            univ[az][ax][ay] = data[0][i][j]
    return univ


def expand(universe, cycles=6):
    cycle = 1
    on = "#"
    off = "."
    while cycle <= cycles:
        current_state = universe.copy()
        for z in range(len(universe)):
            for x in range(len(universe[0])):
                for y in range(len(universe[0][0])):
                    active_cells = count_active_neighbors(universe, z, x, y)
                    if universe[z, x, y] == on:
                        if active_cells == 2 or active_cells == 3:
                            current_state[z, x, y] = on
                        else:
                            current_state[z, x, y] = off
                    else:
                        if active_cells == 3:
                            current_state[z, x, y] = on
                        else:
                            current_state[z, x, y] = off
        cycle += 1
        universe = current_state.copy()
    return universe


def count_active_neighbors(universe, z, x, y):
    counter = 0
    if z == 0:
        zs = 0
    else:
        zs = 1
    if x == 0:
        zx = 0
    else:
        zx = 1
    if y == 0:
        zy = 0
    else:
        zy = 1
    for az in range(z - zs, z + 2):
        for ax in range(x - zx, x + 2):
            for ay in range(y - zy, y + 2):
                if az >= len(universe) or ax >= len(universe[0]) or ay >= len(universe[0][0]):
                    continue
                if az == z and ax == x and ay == y:
                    continue

                else:
                    if universe[az, ax, ay] == "#":
                        counter += 1
    return counter


# -------------------------PART 2------------------------------------------

def create_4d_universe(data, multi=15):
    w = 1
    z = 1
    x = len(data[0])
    y = len(data[0][0])
    univ = np.empty((w * multi, z * multi, x * multi, y * multi), dtype=str)
    az = multi // 2
    aw = multi // 2
    for i in range(x):
        ax = x * multi // 2 + i - 1
        for j in range(y):
            ay = y * multi // 2 + j - 1
            univ[aw][az][ax][ay] = data[0][i][j]
    return univ


def count_active_4d_neighbors(universe, w, z, x, y):
    counter = 0
    if z == 0:
        zs = 0
    else:
        zs = 1
    if x == 0:
        zx = 0
    else:
        zx = 1
    if y == 0:
        zy = 0
    else:
        zy = 1
    if w == 0:
        ws = 0
    else:
        ws = 1
    for aw in range(w - ws, w + 2):
        for az in range(z - zs, z + 2):
            for ax in range(x - zx, x + 2):
                for ay in range(y - zy, y + 2):
                    if aw >= len(universe) or az >= len(universe[0]) or ax >= len(universe[0, 0]) or ay >= len(
                            universe[0, 0, 0]):
                        continue
                    if az == z and ax == x and ay == y and aw == w:
                        continue

                    else:
                        if universe[aw, az, ax, ay] == "#":
                            counter += 1
    return counter

def expand_4d(universe, cycles=6):
    cycle = 1
    on = "#"
    off = "."
    while cycle <= cycles:
        print(f"cycle: {cycle}")
        current_state = universe.copy()
        for w in range(len(universe)):
            for z in range(len(universe[0])):
                for x in range(len(universe[0,0])):
                    for y in range(len(universe[0,0,0])):
                        active_cells = count_active_4d_neighbors(universe, w, z, x, y)
                        if universe[w, z, x, y] == on:
                            if active_cells == 2 or active_cells == 3:
                                current_state[w, z, x, y] = on
                            else:
                                current_state[w, z, x, y] = off
                        else:
                            if active_cells == 3:
                                current_state[w, z, x, y] = on
                            else:
                                current_state[w, z, x, y] = off
        cycle += 1
        universe = current_state.copy()
    return universe


def main():
    example = "example"
    real = "input"
    inp = read(real)
    # pocket = create_universe(inp)
    # final_univ = expand(pocket)
    # print(np.count_nonzero(final_univ == "#"))

    pocket4d = create_4d_universe(inp)
    final_univ = expand_4d(pocket4d)
    print(np.count_nonzero(final_univ == "#"))

if __name__ == '__main__':
    main()
