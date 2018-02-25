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
    # TODO
    return z;

def forward(pos):
    """
        Moving forward in the grid, depending on the actual position
        and the constraints of the grid.
    """
    # TODO
    return pos;

def move(pos, i):
    """
        Determines the new position in the grid,
        depending on the possibles actions allowed.
    """
    if i == 'F':
        pos = forward(pos)
    elif i == 'R' or i == 'L':
        pos[2] = rotate(pos[2], i)
    else:
        print('Invalid Input')

    return pos;

# test file #2
#2 2
#2 0 N
#FFRF

# Algo :
# <pos = def move(pos, i)>
# pos = [2, 1, N] = def move(pos, F)
# pos = [2, 2, N] = def move(pos, F)
# pos = [2, 2, R] = def move(pos, R)
# pos = [2, 2, R] = def move(pos, F)
# ==> [2, 2, R]
pos = [2, 0, 'N'];

pos = move(pos, 'F');
print('pos : %s' % pos);
