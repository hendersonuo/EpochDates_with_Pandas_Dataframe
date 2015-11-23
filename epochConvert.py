from __future__ import division
import datetime
#import time
import pandas as pd
import numpy as np
import random


d3 = pd.read_csv('/Users/MessyJesse/Desktop/d3code/d3.csv')


print """
BEFORE:

"""
print d3.head()

weeks = d3.week #Here I create a Series of just weeks

# Rename columns
d3.columns =[
    'Sun', 'Mon', 'Tues', 'Weds','Thurs',
    'Fri', 'Sat', 'Total', 'Week']


dates = []
months = []

# For each epoch date, standardize format and apnd. to empty list 'dates' (for df collumn)
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
    
for date in weeks:
    x = datetime.datetime.fromtimestamp(date).strftime('%m')
    for a, b in option.items():
        if a == x:
            months.append(b)
   

d3['Week'] = dates #Replace epoch dates with reformatted dates

d3['Month'] = months #This was created by my loop


cols = d3.columns.tolist()
colsList = [8, 9, 0, 1, 2, 3, 4, 5, 6, 7] #Here I rearrange the order of columns
cols = [cols[a] for a in colsList]

d3 = d3[cols] #reset d3


print """
XXX 
XXX
XXX
"""

#BELOW ARE 2 WAYS TO TRIM THE 'Weeks' Collumn off dataframe 'd3'

#d5 = pd.concat([d3.Sun,d3.Mon, d3.Tues, d3.Weds, d3.Thurs, d3.Fri, d3.Sat], axis=1)
#d5 = d3.drop(['Week', 'Total'], axis=1)
#d5 = d3[['Sun','Mon','Tues','Weds','Thurs','Fri','Sat']]



d3['rowAvg'] = d3[['Sun','Mon','Tues','Weds','Thurs','Fri','Sat']].mean(axis=1) #How to make a new collumn with the average of all rows
print d3

print """
XXX 
XXX
XXX
"""

d3means = d3.mean()

#print "The means are...\n", d3means

'''
EXPLORATIONS TO CONSIDER:
1.  weekly means v.s daily means
2. Ways to remove outliers: IQR? This is shown by d3.describe()
3. Histograms and graphs
'''

print """
XXX 
XXX
XXX
"""

print d3.describe()

print """
XXX 
XXX
XXX
"""

d6 = d3[['Week','Total']]
d6.set_index('Week')
d6.plot()

#The next thing is to figure out how to plot this
rand = [random.random() for a in range(10)]
print rand
