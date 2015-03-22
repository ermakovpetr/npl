#!/usr/bin/env python
# coding=utf-8
import sys
import happybase

N = 94

connection = happybase.Connection('ec2-52-16-15-152.eu-west-1.compute.amazonaws.com')
table = connection.table('petr.ermakov')


for line in sys.stdin:
    line = line.strip()

    try:
        uid, timestamp, url = line.split("\t")
        uid = int(uid)
        timestamp = int(float(timestamp) * 1000)
        if not url.strip(): raise ValueError
    except ValueError:
        continue
    
    if uid % 256 == N:
        table.put(str(uid), {'data:url': url}, timestamp=timestamp)


connection.close()
