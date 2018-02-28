#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=old-style-class,invalid-name,no-self-use
"""
The functions about the mower's positions.
"""

from __future__ import print_function

class Mower:
    """
        The class about the mower.
    """

    def __init__(self, MAX_X, MAX_Y):
        self.MAX_X = int(MAX_X)
        self.MAX_Y = int(MAX_Y)

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

    def forward(self, pos, res):
        """
            Moving forward in the grid, depending on the actual position
            and the constraints of the grid.
        """
        xs = []
        ys = []
        for r in res:
            xs.append(r[0])
            ys.append(r[1])

        z = pos[2]
        if z == 'N':
            if pos[1] < self.MAX_Y and pos[1]+1 not in ys:
                pos[1] += 1
        elif z == 'E':
            if pos[0] < self.MAX_X and pos[0]+1 not in xs:
                pos[0] += 1
        elif z == 'W':
            if pos[0] > 0 and pos[0]-1 not in xs:
                pos[0] -= 1
        elif z == 'S':
            if pos[1] > 0 and pos[1]-1 not in ys:
                pos[1] -= 1
        else:
            print('Invalid orientation')
        return pos

    def move(self, pos, i, res):
        """
            Determines the new position in the grid,
            depending on the allowed actions.
        """
        if i == 'F':
            pos = self.forward(pos, res)
        elif i == 'R' or i == 'L':
            pos[2] = self.rotate(pos[2], i)
        else:
            print('Invalid input')
        return pos
