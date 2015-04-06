#!/usr/bin/env python
# coding=utf-8
import sys

for line in sys.stdin:
    line = line.strip()

    try:
        uid, timestamp, url = line.split("\t")
        uid = int(uid)
        if not timestamp.strip(): raise ValueError
        if not url.strip(): raise ValueError
    except ValueError:
        continue

    print(url)
