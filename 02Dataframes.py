# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 12:15:55 2021

@author: ed006315
"""

import pandas as pd

df = pd.DataFrame(np.random.randn(5, 3), columns=list('ABC'))
# i A	        B	        C
# 0	-0.354475	-0.168315	0.124089
# 1	0.111897	-0.035394	0.550676
# 2	0.158766	0.125702	-1.167275
# 3	1.484724	0.141895	-1.599715
# 4	1.656473	-1.015866	-0.796449


df = pd.DataFrame(np.arange(48).reshape(8,6),columns=list('ABCDEF'))
#     A   B   C   D   E   F
# 0   0   1   2   3   4   5
# 1   6   7   8   9  10  11
# 2  12  13  14  15  16  17
# 3  18  19  20  21  22  23
# 4  24  25  26  27  28  29
# 5  30  31  32  33  34  35
# 6  36  37  38  39  40  41
# 7  42  43  44  45  46  47


d = {'dates': pd.date_range(start='1/1/2015', end='11/1/2020', freq='MS').values,
    'series1': np.random.randn(71,),
    'series2': np.random.geometric(p=0.35, size=71)}
df = pd.DataFrame(data=d)
# date range with values for forecasting


fig, ax = plt.subplots()

df.plot(x='dates', kind='line',ax=ax, fontsize=10, sort_columns=True, legend=None)
ax.grid(axis='x')
plt.annotate('Series 1', xy=(df.dates.iloc[-12], df.series1.mean()-2), xycoords='data')
plt.annotate('Series 1', xy=(df.dates.iloc[-12], df.series2.mean()+3), xycoords='data')
plt.text(df.dates.mean(), 0.5, 'Some Text', ha='center', va='center',rotation='vertical', backgroundcolor='white')
plt.show()



df.ix[::2,0] = np.nan # in column 0, set elements with indices 0,2,4, ... to NaN
df.ix[::4,1] = pd.NaT # in column 1, set elements with indices 0,4, ... to np.NaT
df.ix[:3,2] = 'nan'   # in column 2, set elements with index from 0 to 3 to 'nan'
df.ix[:,5] = None     # in column 5, set all elements to None
df.ix[5,:] = None     # in row 5, set all elements to None
df.ix[7,:] = np.nan   # in row 7, set all elements to NaN
#     A     B     C   D   E     F
# 0 NaN   NaT   nan   3   4  None
# 1   6     7   nan   9  10  None
# 2 NaN    13   nan  15  16  None
# 3  18    19   nan  21  22  None
# 4 NaN   NaT    26  27  28  None
# 5 NaN  None  None NaN NaN  None
# 6 NaN    37    38  39  40  None
# 7 NaN   NaN   NaN NaN NaN   NaN
