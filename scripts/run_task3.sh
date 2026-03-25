#!/bin/bash
source /etc/profile.d/hadoop.sh
hdfs dfs -rm -r /user/${USER}/project/m1/task3 2>/dev/null
mapred streaming \
    -files map_location.py,count_reducer.py \
    -mapper "python3 map_location.py" \
    -reducer "python3 count_reducer.py" \
    -input /data/chicago_crimes.csv \
    -output /user/${USER}/project/m1/task3
hdfs dfs -cat /user/${USER}/project/m1/task3/part-00000
