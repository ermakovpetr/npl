Task:  __Count the number of each numbers__

numbers.txt:
```
1673
676
1861
806
610
1878
842
110
794
1764
813
47
1591
1374
2002
779
```

---

Prepare commands
```bash
hadoop fs -mkdir -p /users/numbers
hadoop fs -put /tmp/numbers.txt /users/numbers/
```

Command for start
```bash
hadoop jar hadoop-streaming.jar \
    -input /users/numbers \
    -output /users/numbers/result \
    -mapper "cat" \
    -reducer "uniq -c"
```

Command to view the last 10 lines of the result
```bash
hadoop fs -cat /users/numbers/result/* | sort | tail
```

Result (last 10 lines)
```
  49995 9
  49996 7
  49996 8
  49997 5
  49997 6
  49998 3
  49998 4
  49999 1
  49999 2
  50000 0
```
