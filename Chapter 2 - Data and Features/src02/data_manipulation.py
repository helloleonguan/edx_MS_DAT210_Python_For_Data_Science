# -*- coding: utf-8 -*-
"""
Created on Fri Jun 02 17:04:30 2017

@author: Liyang(Leon) Guan
"""

import pandas as pd

df = pd.read_csv('direct_marketing.csv')

# slicing
print df.recency


#>>> df.recency
#>>> df['recency']
#>>> df[['recency']]
#>>> df.loc[:, 'recency']
#>>> df.loc[:, ['recency']]
#>>> df.iloc[:, 0]
#>>> df.iloc[:, [0]]
#>>> df.ix[:, 0]

# nested slicing produces a dataframe, others produce a series

# expected order: [row_indexer, column_indexer]:
    
# The last important difference is that .loc[] and .ix[] are inclusive 
# of the range of values selected, where .iloc[] is non-inclusive.

# a series of bools
print df.recency < 7

# a dataframe of original data, use bit-wise &, | in []
print df[ df.recency < 7 ]

# update data
# df[df.recency < 7] = -100