#!/bin/bash
source /etc/profile.d/hadoop.sh
hdfs dfs -rm -r /user/${USER}/project/m1/task4 2>/dev/null
mapred streaming \
    -files map_year.py,count_reducer.py \
    -mapper "python3 map_year.py" \
    -reducer "python3 count_reducer.py" \
    -input /data/chicago_crimes.csv \
    -output /user/${USER}/project/m1/task4
hdfs dfs -cat /user/${USER}/project/m1/task4/part-00000
