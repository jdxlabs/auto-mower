#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=wildcard-import

"""
The script to generate mower's final coordinates.
"""

from __future__ import print_function
import os
import sys
from mower import *

if len(sys.argv) < 2:
    quit('Please indicate a filename, like this : ./gen_result.py <filename>')

ENV = os.environ['ENV'] if ('ENV' in os.environ) else 'dev'
if ENV != 'dev' and ENV != 'prod':
    quit('Please indicate a valid environment')

path = './inputs/%s/%s' % (ENV, sys.argv[1])

pos_list = []
inputs_list = []

# extracts instructions from file
try:
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
except IOError:
    quit("The filename you specified doesn't match.")
except ValueError:
    quit("There's something wrong about the mower's instructions.")

if len(pos_list) != len(inputs_list):
    quit("Ensure there's a correct couple of instructions for each mower.")

nmax = len(pos_list)
mower = Mower(MAX_X, MAX_Y)

res = []
for n in range(0, nmax):
    for i in inputs_list[n]:
        pos = mower.move(pos_list[n], i, res)
    res.append(pos)

# outputs expected format
for r in res:
    print("%d %d %s" % (r[0], r[1], r[2]))
