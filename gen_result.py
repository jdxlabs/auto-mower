#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The script to generate mower's final coordinates.
"""

from __future__ import print_function
from mower import *

MAX_X = 2
MAX_Y = 2

pos = [2, 0, 'N']
inputs = ['F', 'F', 'R', 'F']

mower = Mower(MAX_X, MAX_Y)

for i in inputs:
    pos = mower.move(pos, i)
print('pos : %s' % pos)
# [2, 2, E]
