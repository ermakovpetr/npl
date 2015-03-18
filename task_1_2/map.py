#!/usr/bin/env python
# coding=utf-8
import sys

for line in sys.stdin:
    line = line.strip()
    _, _, country, _, payout = line.split(', ')
    print('{}\t{}'.format(country, payout))
