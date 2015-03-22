Task:  __Export data from log-files from Amazon S3 to HBase__

**Structure data in S3**:

Folders ```s3n://newprolab/facetz_YYYY_MM_DD/``` with log-files ```part-NNNN```

**Structure log-files**:

```UID timestamp URL``` and ```'\t'``` - separator

**Other**:

1. Read files only from this folders: ```facetz_2015_02_01```, ```facetz_2015_02_02```, ```facetz_2015_02_03```, ```facetz_2015_02_04```, ```facetz_2015_02_05```

2. Ignore incorrect formatted lines

3. Export only lines with UID with property: ```UID mod 256 = N``` where ```N``` - individual number

4. Table name: ```FIRST_NAME.LAST_NAME```

5. The contents of the table: ```rowkey=uid```, ```column=data:url```, value ```timestamp``` - from log-files 

---

Create table command (in __hbase shell__)
```
create 'petr.ermakov', {NAME => 'data'}
```

Command for start
```bash
hadoop jar hadoop-streaming.jar \
    -input s3n://newprolab/facetz_2015_02_0[1-5] \
    -output non_existent_folder \
    -mapper "./map.py" \
    -file map.py
```
