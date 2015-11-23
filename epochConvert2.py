from __future__ import division
import datetime
import pandas as pd
import numpy as np
import random


d3 = pd.read_csv('/Users/MessyJesse/Desktop/d3code/d3.csv')

print """
BEFORE:
"""
print d3.head()
print

weeks = d3.week #Here I create a Series of just weeks

# Rename columns
d3.columns =[
    'Sun', 'Mon', 'Tues', 'Weds','Thurs',
    'Fri', 'Sat', 'Total', 'Week']


dates = []
months = []

# Standardize epoch digits and place in 'dates'
for date in weeks:
    dates.append(datetime.datetime.fromtimestamp(date).strftime('%Y-%m-%d')) 

option = {
           '01' : 'Jan',
           '02' : 'Feb',
           '03' : 'Mar',
           '04' : 'Apr',
           '05' : 'May',
           '06' : 'Jun',
           '07' : 'Jul',
           '08' : 'Aug',
           '09' : 'Sep',
           '10' : 'Oct',
           '11' : 'Nov',
           '12' : 'Dec'
         }

# Use above dict to convert digit month into English \
# abbreviation and place in 'months'
for date in weeks:
    x = datetime.datetime.fromtimestamp(date).strftime('%m')
    for a, b in option.items():
        if a == x:
            months.append(b)
   
# Create columns with your newly standarized values
d3['Week'] = dates 
d3['Month'] = months

#  Rearrange the order of columns...
cols = d3.columns.tolist()
colsList = [8, 9, 0, 1, 2, 3, 4, 5, 6, 7]
cols = [cols[a] for a in colsList]
d3 = d3[cols] 

# How to make a new collumn = the AVG of all rows
d3['rowAvg'] = d3[['Sun','Mon','Tues','Weds','Thurs','Fri','Sat']].mean(axis=1)

d3.append(d3.sum(numeric_only=True), ignore_index=True)

print """
AFTER:
"""
print d3.head()

#print d3.describe()
