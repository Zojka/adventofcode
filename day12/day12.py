#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: zparteka
"""
import numpy as np

def read_instructions(infile):
    with open(infile, 'r') as f:
        instructions = []
        data = f.readlines()
        for i in data:
            instruction = i.strip()
            instructions.append((instruction[0], int(instruction[1:])))
    return instructions


def follow_instructions(instructions):
    north = 0
    east = 0
    direction = "E"
    degrees = 90
    for i in instructions:
        print(north, east, direction, degrees)
        print(i)
        if i[0] == "L" or i[0] == "R":
            direction, degrees = change_direction(move=i, degrees=degrees)
        elif i[0] == "F":
            north, east = move_forward(north, east, i[1], direction)
        elif i[0] == "N":
            north += i[1]
        elif i[0] == "S":
            north -= i[1]
        elif i[0] == "E":
            east += i[1]
        elif i[0] == "W":
            east -= i[1]
    return abs(north) + abs(east)


def change_direction(move, degrees):
    if move[0] == "R":
        degrees += move[1]
        if degrees >= 360:
            degrees -= 360
    elif move[0] == "L":
        degrees -= move[1]
        if degrees < 0:
            degrees = 360 + degrees
    if degrees == 90:
        return "E", degrees
    elif degrees == 180:
        return "S", degrees
    elif degrees == 270:
        return "W", degrees
    else:
        return "N", degrees


def move_forward(north, east, move, direction):
    if direction == "E":
        east += move
    elif direction == "W":
        east -= move
    elif direction == "S":
        north -= move
    else:
        north += move
    return north, east


def part2(instructions):
    ship_north = 0
    ship_east = 0
    point_east = 10
    point_north = 1
    direction = "E"
    degrees = 90
    for i in instructions:
        if i[0] == "F":
            ship_east += i[1] * point_east
            ship_north += i[1] * point_north
        elif i[0] == "N":
            point_north += i[1]
        elif i[0] == "S":
            point_north -= i[1]
        elif i[0] == "E":
            point_east += i[1]
        elif i[0] == "W":
            point_east -= i[1]
        elif i[0] == "R":
            theta = np.radians(i[1])
            c, s = np.cos(theta), np.sin(theta)
            R = np.array(((c, -s), (s, c)))
            point_north, point_east =  np.matmul(R, np.asarray((point_north, point_east)))
            point_east = round(point_east)
            point_north = round(point_north)
        elif i[0] == "L":
            theta = np.radians(i[1])
            c, s = np.cos(theta), np.sin(theta)
            R = np.array(((c, s), (-s, c)))
            point_north, point_east =  np.matmul(R, np.asarray((point_north, point_east)))
            point_east = round(point_east)
            point_north = round(point_north)
    return abs(ship_north) + abs(ship_east)



def main():
    infile = "input12"
    instructions = read_instructions(infile)
    # print(instructions)
    # print(follow_instructions(instructions))
    example = "example"
    exam2 = read_instructions(example)
    print(part2(instructions))

if __name__ == "__main__":
    main()
