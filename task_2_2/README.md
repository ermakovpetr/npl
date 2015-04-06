Task:  __From log-files from Amazon S3 export top 350 urls__

**Structure data in S3**:

Folders ```s3n://newprolab/facetz_YYYY_MM_DD/``` with log-files ```part-NNNN```

**Structure log-files**:

```UID timestamp URL``` and ```'\t'``` - separator

**Other**:

1. Read files only from this folder ```facetz_2015_02_03```

2. Ignore incorrect formatted lines

3. Export top 350 urls to ```top350.txt```

4. The contents of the file: ```COUNT URL``` and ```'\t'``` - separator

5. Use command ```sort```

---

Command for start
```bash
hadoop jar hadoop-streaming.jar \
    -input s3n://newprolab/facetz_2015_02_03 \
    -output top_temp \
    -mapper "./map.py" \
    -file map.py \
    -combiner "uniq -c" \
    -reducer "uniq -c"
```

Command for prepare result
```bash
hdfs dfs -cat top_temp/* \
    | sort -n -r -T /mnt/tmp/ \
    | head -350 \
    | sed 's/\s*\([0-9]*\)\s*\(\S*\)/\2\t\1/g' \
    > top350.txt
```
