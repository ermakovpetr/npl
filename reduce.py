#!/usr/bin/env python
# coding=utf-8
import sys

last_country = None
total_payout = 0

for line in sys.stdin:
    line = line.strip()
    country, payout = line.split('\t')
    payout = float(payout)
    if last_country is None:
        last_country = country

    if country == last_country:
        total_payout += payout
    else:
        print('{}\t{}'.format(last_country, total_payout))
        last_country = country
        total_payout = payout

print('{}\t{}'.format(last_country, total_payout))
