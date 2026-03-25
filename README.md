# SE446 - Chicago Crime Analytics with MapReduce

## Group Name: Big Data Guys

## Team Members

| Name | Student ID |
|------|-----------|
| Abdulrahman Alghannam | 220455 |
| Abdulmohsen Binkhamis | 230241 |
| Saud Aldawood | 230336 |
| Feras Alkahtani | 230313 |
| Khalid Aleisa | 230525 |

## Executive Summary

We built a set of MapReduce jobs to analyze the Chicago Crime dataset on our Hadoop cluster. The pipeline consists of task-specific mappers that extract fields from each CSV row and a shared reducer that sums up counts per key. We ran all jobs against the full dataset at `/data/chicago_crimes.csv` using Hadoop Streaming. Each group member was responsible for writing and running their assigned task on the cluster under their own user account.

## Project Structure

```
src/          - MapReduce source code (mappers and reducer)
scripts/      - Shell scripts for cluster execution
output/       - Results from cluster runs
```

---

## Task 2: Crime Type Distribution

**Assigned to:** Abdulrahman Alghannam (abalghannam)

**Research Question:** What are the most common types of crimes in Chicago?

**Implementation:** `map_crimetype.py` reads each line from stdin, splits by comma, skips the header, and extracts the Primary Type field at index 5. It prints the crime type with a count of 1. The reducer sums up all counts per crime type.

**Execution Command (Abdulrahman):**
```bash
source /etc/profile.d/hadoop.sh

mapred streaming \
  -files map_crimetype.py,count_reducer.py \
  -mapper "python3 map_crimetype.py" \
  -reducer "python3 count_reducer.py" \
  -input /data/chicago_crimes.csv \
  -output /user/abalghannam/project/m1/task2
```

**Execution Command (Khalid):**
```bash
source /etc/profile.d/hadoop.sh

mapred streaming \
  -files map_crimetype.py,count_reducer.py \
  -mapper "python3 map_crimetype.py" \
  -reducer "python3 count_reducer.py" \
  -input /data/chicago_crimes.csv \
  -output /user/kaleissa/project/m1/task2
```

**Sample Results (Top 5):**
```
THEFT           162688
BATTERY         151930
CRIMINAL DAMAGE  91241
NARCOTICS        74127
ASSAULT          54070
```

**Interpretation:** Theft leads all crime categories with 162,688 reported incidents, followed by Battery at 151,930. These two categories together make up a large share of total crime, suggesting property theft and physical altercations are the biggest concerns for resource allocation.

**Execution Log (abalghannam):**
```
packageJobJar: [] [/opt/hadoop-3.4.1/share/hadoop/tools/lib/hadoop-streaming-3.4.1.jar] /tmp/streamjob5198397707633661563.jar tmpDir=null
2026-03-25 10:04:48,129 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at master-node/134.209.172.50:8032
2026-03-25 10:04:48,482 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at master-node/134.209.172.50:8032
2026-03-25 10:04:49,003 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/abalghannam/.staging/job_1771402826595_0187
2026-03-25 10:04:51,529 INFO mapred.FileInputFormat: Total input files to process : 1
2026-03-25 10:04:51,594 INFO net.NetworkTopology: Adding a new node: /default-rack/146.190.147.119:9866
2026-03-25 10:04:51,606 INFO net.NetworkTopology: Adding a new node: /default-rack/164.92.103.148:9866
2026-03-25 10:04:52,700 INFO mapreduce.JobSubmitter: number of splits:2
2026-03-25 10:04:53,695 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1771402826595_0187
2026-03-25 10:04:53,695 INFO mapreduce.JobSubmitter: Executing with tokens: []
2026-03-25 10:04:54,004 INFO conf.Configuration: resource-types.xml not found
2026-03-25 10:04:54,005 INFO resource.ResourceUtils: Unable to find 'resource-types.xml'.
2026-03-25 10:04:54,141 INFO impl.YarnClientImpl: Submitted application application_1771402826595_0187
2026-03-25 10:04:54,200 INFO mapreduce.Job: The url to track the job: http://master-node:8088/proxy/application_1771402826595_0187/
2026-03-25 10:04:54,202 INFO mapreduce.Job: Running job: job_1771402826595_0187
2026-03-25 10:05:12,967 INFO mapreduce.Job: Job job_1771402826595_0187 running in uber mode : false
2026-03-25 10:05:12,969 INFO mapreduce.Job:  map 0% reduce 0%
2026-03-25 10:05:38,350 INFO mapreduce.Job:  map 100% reduce 0%
2026-03-25 10:05:53,850 INFO mapreduce.Job:  map 100% reduce 100%
2026-03-25 10:05:56,622 INFO mapreduce.Job: Job job_1771402826595_0187 completed successfully
2026-03-25 10:05:56,891 INFO mapreduce.Job: Counters: 54
        File System Counters
                FILE: Number of bytes read=11798790
                FILE: Number of bytes written=24540863
                HDFS: Number of bytes read=181964998
                HDFS: Number of bytes written=690
                HDFS: Number of read operations=11
                HDFS: Number of write operations=2
        Job Counters
                Launched map tasks=2
                Launched reduce tasks=1
                Data-local map tasks=2
                Total time spent by all maps in occupied slots (ms)=90576
                Total time spent by all reduces in occupied slots (ms)=25750
        Map-Reduce Framework
                Map input records=793074
                Map output records=793072
                Map output bytes=10212640
                Map output materialized bytes=11798796
                Reduce input groups=34
                Reduce input records=793072
                Reduce output records=34
                Spilled Records=1586144
        File Input Format Counters
                Bytes Read=181964800
        File Output Format Counters
                Bytes Written=690
2026-03-25 10:05:56,892 INFO streaming.StreamJob: Output directory: /user/abalghannam/project/m1/task2
```

**Execution Log (Khalid - kaleissa):**
```
packageJobJar: [] [/opt/hadoop-3.4.1/share/hadoop/tools/lib/hadoop-streaming-3.4.1.jar] /tmp/streamjob13653920879372862374.jar tmpDir=null
2026-03-25 16:15:39,267 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at master-node/134.209.172.50:8032
2026-03-25 16:15:39,604 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at master-node/134.209.172.50:8032
2026-03-25 16:15:40,093 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/kaleissa/.staging/job_1771402826595_0218
2026-03-25 16:15:41,928 INFO mapred.FileInputFormat: Total input files to process : 1
2026-03-25 16:15:41,961 INFO net.NetworkTopology: Adding a new node: /default-rack/164.92.103.148:9866
2026-03-25 16:15:41,962 INFO net.NetworkTopology: Adding a new node: /default-rack/146.190.147.119:9866
2026-03-25 16:15:42,563 INFO mapreduce.JobSubmitter: number of splits:2
2026-03-25 16:15:43,457 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1771402826595_0218
2026-03-25 16:15:43,457 INFO mapreduce.JobSubmitter: Executing with tokens: []
2026-03-25 16:15:43,852 INFO conf.Configuration: resource-types.xml not found
2026-03-25 16:15:43,853 INFO resource.ResourceUtils: Unable to find 'resource-types.xml'.
2026-03-25 16:15:44,009 INFO impl.YarnClientImpl: Submitted application application_1771402826595_0218
2026-03-25 16:15:44,075 INFO mapreduce.Job: The url to track the job: http://master-node:8088/proxy/application_1771402826595_0218/
2026-03-25 16:15:44,078 INFO mapreduce.Job: Running job: job_1771402826595_0218
2026-03-25 16:16:00,770 INFO mapreduce.Job: Job job_1771402826595_0218 running in uber mode : false
2026-03-25 16:16:00,772 INFO mapreduce.Job:  map 0% reduce 0%
2026-03-25 16:16:28,717 INFO mapreduce.Job:  map 100% reduce 0%
2026-03-25 16:16:42,122 INFO mapreduce.Job:  map 100% reduce 100%
2026-03-25 16:16:44,974 INFO mapreduce.Job: Job job_1771402826595_0218 completed successfully
2026-03-25 16:16:45,237 INFO mapreduce.Job: Counters: 54
        File System Counters
                FILE: Number of bytes read=11798790
                FILE: Number of bytes written=24540749
                HDFS: Number of bytes read=181964998
                HDFS: Number of bytes written=690
                HDFS: Number of read operations=11
                HDFS: Number of write operations=2
        Job Counters
                Launched map tasks=2
                Launched reduce tasks=1
                Data-local map tasks=2
                Total time spent by all maps in occupied slots (ms)=101426
                Total time spent by all reduces in occupied slots (ms)=21346
        Map-Reduce Framework
                Map input records=793074
                Map output records=793072
                Map output bytes=10212640
                Map output materialized bytes=11798796
                Reduce input groups=34
                Reduce input records=793072
                Reduce output records=34
                Spilled Records=1586144
        File Input Format Counters
                Bytes Read=181964800
        File Output Format Counters
                Bytes Written=690
2026-03-25 16:16:45,237 INFO streaming.StreamJob: Output directory: /user/kaleissa/project/m1/task2
```

**Full Output:**
```
ARSON	1717
ASSAULT	54070
BATTERY	151930
BURGLARY	39872
CONCEALED CARRY LICENSE VIOLATION	77
CRIM SEXUAL ASSAULT	2463
CRIMINAL DAMAGE	91241
CRIMINAL SEXUAL ASSAULT	1372
CRIMINAL TRESPASS	21476
DECEPTIVE PRACTICE	30396
DOMESTIC VIOLENCE	1
GAMBLING	1314
HOMICIDE	13173
HUMAN TRAFFICKING	13
INTERFERENCE WITH PUBLIC OFFICER	803
INTIMIDATION	92
KIDNAPPING	1108
LIQUOR LAW VIOLATION	2349
MOTOR VEHICLE THEFT	48494
NARCOTICS	74127
NON-CRIMINAL	1
OBSCENITY	24
OFFENSE INVOLVING CHILDREN	2065
OTHER NARCOTIC VIOLATION	11
OTHER OFFENSE	36893
PROSTITUTION	9100
PUBLIC INDECENCY	17
PUBLIC PEACE VIOLATION	1827
RITUALISM	8
ROBBERY	30991
SEX OFFENSE	3932
STALKING	534
THEFT	162688
WEAPONS VIOLATION	8893
```

---

## Task 3: Location Hotspots

**Assigned to:** Abdulmohsen Binkhamis (abinkhamis)

**Research Question:** Where do most crimes occur?

**Implementation:** `map_location.py` extracts the Location Description field at index 7 from each CSV row and emits it with a count of 1. The reducer aggregates totals per location type.

**Execution Command:**
```bash
source /etc/profile.d/hadoop.sh

mapred streaming \
  -files map_location.py,count_reducer.py \
  -mapper "python3 map_location.py" \
  -reducer "python3 count_reducer.py" \
  -input /data/chicago_crimes.csv \
  -output /user/abinkhamis/project/m1/task3
```

**Sample Results (Top 5):**
```
STREET      245437
RESIDENCE   136238
APARTMENT    60925
SIDEWALK     47407
OTHER        29213
```

**Interpretation:** The street is the most common crime location by a wide margin with 245,437 incidents, more than the next two locations combined. Residences and apartments follow, indicating that both public outdoor areas and private dwellings are high-risk zones. Patrol units should focus on street-level presence to maximize coverage.

**Execution Log (abinkhamis):**
```
packageJobJar: [] [/opt/hadoop-3.4.1/share/hadoop/tools/lib/hadoop-streaming-3.4.1.jar] /tmp/streamjob6844517794292286921.jar tmpDir=null
2026-03-25 10:10:51,940 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at master-node/134.209.172.50:8032
2026-03-25 10:10:52,322 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at master-node/134.209.172.50:8032
2026-03-25 10:10:52,836 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/abinkhamis/.staging/job_1771402826595_0188
2026-03-25 10:10:54,693 INFO mapred.FileInputFormat: Total input files to process : 1
2026-03-25 10:10:54,730 INFO net.NetworkTopology: Adding a new node: /default-rack/164.92.103.148:9866
2026-03-25 10:10:54,731 INFO net.NetworkTopology: Adding a new node: /default-rack/146.190.147.119:9866
2026-03-25 10:10:55,397 INFO mapreduce.JobSubmitter: number of splits:2
2026-03-25 10:10:56,203 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1771402826595_0188
2026-03-25 10:10:56,203 INFO mapreduce.JobSubmitter: Executing with tokens: []
2026-03-25 10:10:56,520 INFO conf.Configuration: resource-types.xml not found
2026-03-25 10:10:56,521 INFO resource.ResourceUtils: Unable to find 'resource-types.xml'.
2026-03-25 10:10:56,634 INFO impl.YarnClientImpl: Submitted application application_1771402826595_0188
2026-03-25 10:10:56,680 INFO mapreduce.Job: The url to track the job: http://master-node:8088/proxy/application_1771402826595_0188/
2026-03-25 10:10:56,682 INFO mapreduce.Job: Running job: job_1771402826595_0188
2026-03-25 10:11:14,452 INFO mapreduce.Job: Job job_1771402826595_0188 running in uber mode : false
2026-03-25 10:11:14,455 INFO mapreduce.Job:  map 0% reduce 0%
2026-03-25 10:11:41,303 INFO mapreduce.Job:  map 100% reduce 0%
2026-03-25 10:11:53,454 INFO mapreduce.Job:  map 100% reduce 100%
2026-03-25 10:11:56,319 INFO mapreduce.Job: Job job_1771402826595_0188 completed successfully
2026-03-25 10:11:56,538 INFO mapreduce.Job: Counters: 54
        File System Counters
                FILE: Number of bytes read=12333747
                FILE: Number of bytes written=25610726
                HDFS: Number of bytes read=181964998
                HDFS: Number of bytes written=4749
                HDFS: Number of read operations=11
                HDFS: Number of write operations=2
        Job Counters
                Launched map tasks=2
                Launched reduce tasks=1
                Data-local map tasks=2
                Total time spent by all maps in occupied slots (ms)=92522
                Total time spent by all reduces in occupied slots (ms)=20560
        Map-Reduce Framework
                Map input records=793074
                Map output records=791480
                Map output bytes=10750781
                Map output materialized bytes=12333753
                Reduce input groups=216
                Reduce input records=791480
                Reduce output records=216
                Spilled Records=1582960
        File Input Format Counters
                Bytes Read=181964800
        File Output Format Counters
                Bytes Written=4749
2026-03-25 10:11:56,539 INFO streaming.StreamJob: Output directory: /user/abinkhamis/project/m1/task3
```

**Full Output:**
```
ABANDONED BUILDING	829
AIRCRAFT	34
AIRPORT BUILDING NON-TERMINAL - NON-SECURE AREA	33
AIRPORT BUILDING NON-TERMINAL - SECURE AREA	16
AIRPORT EXTERIOR - NON-SECURE AREA	33
AIRPORT EXTERIOR - SECURE AREA	20
AIRPORT PARKING LOT	81
AIRPORT TERMINAL LOWER LEVEL - NON-SECURE AREA	60
AIRPORT TERMINAL LOWER LEVEL - SECURE AREA	42
AIRPORT TERMINAL MEZZANINE - NON-SECURE AREA	4
AIRPORT TERMINAL UPPER LEVEL - NON-SECURE AREA	41
AIRPORT TERMINAL UPPER LEVEL - SECURE AREA	133
AIRPORT TRANSPORTATION SYSTEM (ATS)	12
AIRPORT VENDING ESTABLISHMENT	7
AIRPORT/AIRCRAFT	2753
ALLEY	18258
ANIMAL HOSPITAL	13
APARTMENT	60925
APPLIANCE STORE	269
ATHLETIC CLUB	465
ATM (AUTOMATIC TELLER MACHINE)	66
AUTO	1370
AUTO / BOAT / RV DEALERSHIP	92
BANK	3325
BAR OR TAVERN	3380
BARBERSHOP	642
BOWLING ALLEY	85
BRIDGE	28
BUS	3085
CAR WASH	363
CHA APARTMENT	8340
CHA HALLWAY/STAIRWELL/ELEVATOR	4773
CHA PARKING LOT/GROUNDS	11846
CHURCH/SYNAGOGUE/PLACE OF WORSHIP	1344
CLEANING STORE	786
COLLEGE/UNIVERSITY GROUNDS	449
COLLEGE/UNIVERSITY RESIDENCE HALL	87
COMMERCIAL / BUSINESS OFFICE	8219
CONSTRUCTION SITE	1206
CONVENIENCE STORE	610
CTA BUS	2147
CTA PLATFORM	4938
CTA TRAIN	1932
CURRENCY EXCHANGE	1277
DAY CARE CENTER	246
DELIVERY TRUCK	149
DEPARTMENT STORE	10818
DRIVEWAY - RESIDENTIAL	1902
DRUG STORE	4469
FACTORY/MANUFACTURING BUILDING	910
FEDERAL BUILDING	85
FIRE STATION	125
FOREST PRESERVE	62
GAS STATION	7703
GOVERNMENT BUILDING/PROPERTY	1447
GROCERY FOOD STORE	13029
HOSPITAL BUILDING/GROUNDS	1962
HOTEL/MOTEL	3166
LIBRARY	585
MEDICAL/DENTAL OFFICE	753
MOVIE HOUSE/THEATER	297
NURSING HOME/RETIREMENT HOME	1538
OFFICE	19
OTHER	29213
OTHER (SPECIFY)	1843
OTHER COMMERCIAL TRANSPORTATION	359
OTHER RAILROAD PROP / TRAIN DEPOT	586
PARK PROPERTY	5745
PARKING LOT/GARAGE(NON.RESID.)	21876
POLICE FACILITY/VEH PARKING LOT	869
RESIDENCE	136238
RESIDENCE - GARAGE	1116
RESIDENCE - PORCH / HALLWAY	1270
RESIDENCE - YARD (FRONT / BACK)	964
RESIDENCE PORCH/HALLWAY	12619
RESIDENCE-GARAGE	14266
RESTAURANT	11996
SCHOOL - PRIVATE BUILDING	123
SCHOOL - PRIVATE GROUNDS	148
SCHOOL - PUBLIC BUILDING	803
SCHOOL - PUBLIC GROUNDS	759
SIDEWALK	47407
SMALL RETAIL STORE	13755
SPORTS ARENA/STADIUM	349
STREET	245437
TAVERN/LIQUOR STORE	3764
TAXICAB	701
VACANT LOT/LAND	1892
VEHICLE NON-COMMERCIAL	7738
VEHICLE-COMMERCIAL	435
WAREHOUSE	1286
YARD	311
```

---

## Task 4: Crime Trends by Year

**Assigned to:** Saud Aldawood (saldawood)

**Research Question:** How has the total number of crimes changed over the years?

**Implementation:** `map_year.py` extracts the Date field at index 2, splits by space to isolate the date portion, then splits by `/` to get the year. Each year is emitted with a count of 1. The reducer sums up all counts per year.

**Execution Command:**
```bash
source /etc/profile.d/hadoop.sh

mapred streaming \
  -files map_year.py,count_reducer.py \
  -mapper "python3 map_year.py" \
  -reducer "python3 count_reducer.py" \
  -input /data/chicago_crimes.csv \
  -output /user/saldawood/project/m1/task4
```

**Sample Results (Top 5 by volume):**
```
2001    467301
2002    205267
2023     81461
2025     12710
2022      4678
```

**Interpretation:** 2001 has the highest recorded crime count at 467,301, with a steep decline in following years. The drop from 2001 to 2002 and onward shows a long-term downward trend. A recent uptick in 2022-2023 is visible, which could reflect changes in reporting or socioeconomic shifts.

**Execution Log (saldawood):**
```
packageJobJar: [] [/opt/hadoop-3.4.1/share/hadoop/tools/lib/hadoop-streaming-3.4.1.jar] /tmp/streamjob10028666633144459002.jar tmpDir=null
2026-03-25 10:13:41,483 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at master-node/134.209.172.50:8032
2026-03-25 10:13:41,760 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at master-node/134.209.172.50:8032
2026-03-25 10:13:42,197 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/saldawood/.staging/job_1771402826595_0189
2026-03-25 10:13:44,316 INFO mapred.FileInputFormat: Total input files to process : 1
2026-03-25 10:13:44,342 INFO net.NetworkTopology: Adding a new node: /default-rack/164.92.103.148:9866
2026-03-25 10:13:44,343 INFO net.NetworkTopology: Adding a new node: /default-rack/146.190.147.119:9866
2026-03-25 10:13:44,995 INFO mapreduce.JobSubmitter: number of splits:2
2026-03-25 10:13:45,755 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1771402826595_0189
2026-03-25 10:13:45,755 INFO mapreduce.JobSubmitter: Executing with tokens: []
2026-03-25 10:13:46,090 INFO conf.Configuration: resource-types.xml not found
2026-03-25 10:13:46,091 INFO resource.ResourceUtils: Unable to find 'resource-types.xml'.
2026-03-25 10:13:46,232 INFO impl.YarnClientImpl: Submitted application application_1771402826595_0189
2026-03-25 10:13:46,290 INFO mapreduce.Job: The url to track the job: http://master-node:8088/proxy/application_1771402826595_0189/
2026-03-25 10:13:46,294 INFO mapreduce.Job: Running job: job_1771402826595_0189
2026-03-25 10:14:03,227 INFO mapreduce.Job: Job job_1771402826595_0189 running in uber mode : false
2026-03-25 10:14:03,229 INFO mapreduce.Job:  map 0% reduce 0%
2026-03-25 10:14:26,569 INFO mapreduce.Job:  map 50% reduce 0%
2026-03-25 10:14:27,835 INFO mapreduce.Job:  map 100% reduce 0%
2026-03-25 10:14:40,251 INFO mapreduce.Job:  map 100% reduce 100%
2026-03-25 10:14:43,203 INFO mapreduce.Job: Job job_1771402826595_0189 completed successfully
2026-03-25 10:14:43,467 INFO mapreduce.Job: Counters: 54
        File System Counters
                FILE: Number of bytes read=7137663
                FILE: Number of bytes written=15218474
                HDFS: Number of bytes read=181964998
                HDFS: Number of bytes written=245
                HDFS: Number of read operations=11
                HDFS: Number of write operations=2
        Job Counters
                Launched map tasks=2
                Launched reduce tasks=1
                Data-local map tasks=2
                Total time spent by all maps in occupied slots (ms)=85092
                Total time spent by all reduces in occupied slots (ms)=20790
        Map-Reduce Framework
                Map input records=793074
                Map output records=793073
                Map output bytes=5551511
                Map output materialized bytes=7137669
                Reduce input groups=25
                Reduce input records=793073
                Reduce output records=25
                Spilled Records=1586146
        File Input Format Counters
                Bytes Read=181964800
        File Output Format Counters
                Bytes Written=245
2026-03-25 10:14:43,467 INFO streaming.StreamJob: Output directory: /user/saldawood/project/m1/task4
```

**Full Output:**
```
2001	467301
2002	205267
2003	985
2004	915
2005	1031
2006	796
2007	762
2008	1010
2009	910
2010	695
2011	770
2012	800
2013	714
2014	825
2015	1105
2016	1339
2017	1387
2018	1327
2019	1174
2020	1832
2021	2399
2022	4678
2023	81461
2024	880
2025	12710
```

---

## Task 5: Law Enforcement Analysis

**Assigned to:** Feras Alkahtani (feaalkahtani)

**Research Question:** What percentage of crimes result in an arrest?

**Implementation:** `map_arrest.py` extracts the Arrest field at index 8 and checks if the value is True or False. It emits the appropriate label with a count of 1. The reducer sums up both categories.

**Execution Command:**
```bash
source /etc/profile.d/hadoop.sh

mapred streaming \
  -files map_arrest.py,count_reducer.py \
  -mapper "python3 map_arrest.py" \
  -reducer "python3 count_reducer.py" \
  -input /data/chicago_crimes.csv \
  -output /user/feaalkahtani/project/m1/task5
```

**Results:**
```
false	551554
true	215199
```

**Interpretation:** Out of 766,753 records with arrest data, only 215,199 (28.1%) led to an arrest while 551,554 (71.9%) did not. This means roughly 7 out of 10 reported crimes go without an arrest, pointing to a gap that could benefit from additional patrol resources or investigative support.

**Execution Log (feaalkahtani):**
```
packageJobJar: [] [/opt/hadoop-3.4.1/share/hadoop/tools/lib/hadoop-streaming-3.4.1.jar] /tmp/streamjob14300159889399711099.jar tmpDir=null
2026-03-25 16:09:52,439 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at master-node/134.209.172.50:8032
2026-03-25 16:09:52,744 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at master-node/134.209.172.50:8032
2026-03-25 16:09:53,270 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/feaalkahtani/.staging/job_1771402826595_0217
2026-03-25 16:09:55,182 INFO mapred.FileInputFormat: Total input files to process : 1
2026-03-25 16:09:55,214 INFO net.NetworkTopology: Adding a new node: /default-rack/146.190.147.119:9866
2026-03-25 16:09:55,215 INFO net.NetworkTopology: Adding a new node: /default-rack/164.92.103.148:9866
2026-03-25 16:09:55,905 INFO mapreduce.JobSubmitter: number of splits:2
2026-03-25 16:09:56,854 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1771402826595_0217
2026-03-25 16:09:56,854 INFO mapreduce.JobSubmitter: Executing with tokens: []
2026-03-25 16:09:57,179 INFO conf.Configuration: resource-types.xml not found
2026-03-25 16:09:57,179 INFO resource.ResourceUtils: Unable to find 'resource-types.xml'.
2026-03-25 16:09:57,310 INFO impl.YarnClientImpl: Submitted application application_1771402826595_0217
2026-03-25 16:09:57,376 INFO mapreduce.Job: The url to track the job: http://master-node:8088/proxy/application_1771402826595_0217/
2026-03-25 16:09:57,379 INFO mapreduce.Job: Running job: job_1771402826595_0217
2026-03-25 16:10:18,399 INFO mapreduce.Job: Job job_1771402826595_0217 running in uber mode : false
2026-03-25 16:10:18,402 INFO mapreduce.Job:  map 0% reduce 0%
2026-03-25 16:10:47,878 INFO mapreduce.Job:  map 100% reduce 0%
2026-03-25 16:11:04,707 INFO mapreduce.Job:  map 100% reduce 100%
2026-03-25 16:11:07,491 INFO mapreduce.Job: Job job_1771402826595_0217 completed successfully
2026-03-25 16:11:07,827 INFO mapreduce.Job: Counters: 55
        File System Counters
                FILE: Number of bytes read=7452337
                FILE: Number of bytes written=15847963
                HDFS: Number of bytes read=181964998
                HDFS: Number of bytes written=25
                HDFS: Number of read operations=11
                HDFS: Number of write operations=2
        Job Counters
                Killed map tasks=1
                Launched map tasks=2
                Launched reduce tasks=1
                Data-local map tasks=2
                Total time spent by all maps in occupied slots (ms)=106742
                Total time spent by all reduces in occupied slots (ms)=25774
        Map-Reduce Framework
                Map input records=793074
                Map output records=766753
                Map output bytes=5918825
                Map output materialized bytes=7452343
                Reduce input groups=2
                Reduce input records=766753
                Reduce output records=2
                Spilled Records=1533506
        File Input Format Counters
                Bytes Read=181964800
        File Output Format Counters
                Bytes Written=25
2026-03-25 16:11:07,827 INFO streaming.StreamJob: Output directory: /user/feaalkahtani/project/m1/task5
```

**Full Output:**
```
false	551554
true	215199
```

---

## Member Contribution

| Member | Task | Role |
|--------|------|------|
| Abdulrahman Alghannam (abalghannam) | Task 2: Crime Type Distribution | Wrote map_crimetype.py, ran job on cluster |
| Abdulmohsen Binkhamis (abinkhamis) | Task 3: Location Hotspots | Wrote map_location.py, ran job on cluster |
| Saud Aldawood (saldawood) | Task 4: Crime Trends by Year | Wrote map_year.py, ran job on cluster |
| Feras Alkahtani (feaalkahtani) | Task 5: Arrest Analysis | Wrote map_arrest.py, ran job on cluster |
| Khalid Aleisa (kaleissa) | Task 2: Crime Type Distribution | Verified and re-ran crime type analysis on cluster, wrote count_reducer.py, shell scripts, README |
