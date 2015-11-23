# Pandas_DataFrame_Cleanup
==========================

1. Reads CSV, converts to Pandas DataFrame
2. Standarizes numeric epoch dates
3. Enhances presentation, so data is better primed for analysis

OUTPUT EXAMPLE:


```python
BEFORE:

   days/0  days/1  days/2  days/3  days/4  days/5  days/6  total        week
0       0       0       0       0       0       0       0      0  1414281600
1       0       1       0       0       0       0       0      1  1414886400
2       0       0       0       0       2       4       3      9  1415491200
3       9       9       4      10       1       0       0     33  1416096000
4       0       1       0       0       0       0       1      2  1416700800


AFTER:

         Week Month  Sun  Mon  Tues  Weds  Thurs  Fri  Sat  Total    rowAvg
0  2014-10-25   Oct    0    0     0     0      0    0    0      0  0.000000
1  2014-11-01   Nov    0    1     0     0      0    0    0      1  0.142857
2  2014-11-08   Nov    0    0     0     0      2    4    3      9  1.285714
3  2014-11-15   Nov    9    9     4    10      1    0    0     33  4.714286
4  2014-11-22   Nov    0    1     0     0      0    0    1      2  0.285714
```
