#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

class Mower:
    """
    The functions about the mower's positions.
    """

    def __init__(self, MAX_X, MAX_Y):
        self.MAX_X = MAX_X
        self.MAX_Y = MAX_Y

    def rotate(self, z, i):
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

    def forward(self, pos):
        """
            Moving forward in the grid, depending on the actual position
            and the constraints of the grid.
        """
        z = pos[2]
        if z == 'N':
            if pos[1] < self.MAX_Y:
                pos[1] += 1
        elif z == 'E':
            if pos[0] < self.MAX_X:
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

    def move(self, pos, i):
        """
            Determines the new position in the grid,
            depending on the allowed actions.
        """
        if i == 'F':
            pos = self.forward(pos)
        elif i == 'R' or i == 'L':
            pos[2] = self.rotate(pos[2], i)
        else:
            print('Invalid input')
        return pos
