#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=wildcard-import

"""
The script to generate mower's final coordinates.
"""

from __future__ import print_function
import sys
from mower import *

if len(sys.argv) < 2:
    quit('Please indicate a filename')
path = './inputs/%s' % sys.argv[1]

pos_list = []
inputs_list = []

# extract instructions from file
with open(path) as f:
    c = 0
    for x in f.readlines():
        l = x.strip().split(' ')
        if c == 0:
            MAX_X = int(l[0])
            MAX_Y = int(l[1])
        else:
            try:
                pos = [int(l[0]), int(l[1]), l[2]]
                pos_list.append(pos)
            except ValueError:
                inputs_list.append(list(l[0]))
        c += 1

if len(pos_list) != len(inputs_list):
    quit("There's something wrong about the mower's instructions.")

nmax = len(pos_list)
mower = Mower(MAX_X, MAX_Y)

res = []
for n in range(0, nmax):
    for i in inputs_list[n]:
        pos = mower.move(pos_list[n], i)
    res.append(pos)

print(res)
# [2, 2, E]
