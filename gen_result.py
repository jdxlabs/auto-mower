#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The script to generate mower's final coordinates.
"""

from __future__ import print_function

MAX_X = 2
MAX_Y = 2

def rotate(z, i):
    """
        Determines the new orientation (z = NEWS),
        depending on the actual orientation and turn input (i = LR).
    """
    if i != 'R' and i != 'L':
        print('Invalid input')
        return z

    if z == 'N':
        z = 'E' if (i == 'R') else 'W'
    elif z == 'E':
        z = 'S' if (i == 'R') else 'N'
    elif z == 'W':
        z = 'N' if (i == 'R') else 'S'
    elif z == 'S':
        z = 'W' if (i == 'R') else 'E'
    else:
        print('Invalid orientation')

    return z

def forward(pos):
    """
        Moving forward in the grid, depending on the actual position
        and the constraints of the grid.
    """
    z = pos[2]
    if z == 'N':
        if pos[1] < MAX_Y:
            pos[1] += 1
    elif z == 'E':
        if pos[0] < MAX_X:
            pos[0] += 1
    elif z == 'W':
        if pos[0] > 0:
            pos[0] -= 1
    elif z == 'S':
        if pos[1] > 0:
            pos[1] -= 1
    else:
        print('Invalid orientation')

    return pos

def move(pos, i):
    """
        Determines the new position in the grid,
        depending on the allowed actions.
    """
    if i == 'F':
        pos = forward(pos)
    elif i == 'R' or i == 'L':
        pos[2] = rotate(pos[2], i)
    else:
        print('Invalid input')

    return pos

pos = [2, 0, 'N']
pos = move(pos, 'F')
pos = move(pos, 'F')
pos = move(pos, 'R')
pos = move(pos, 'F')
print('pos : %s' % pos)
# [2, 2, E]
