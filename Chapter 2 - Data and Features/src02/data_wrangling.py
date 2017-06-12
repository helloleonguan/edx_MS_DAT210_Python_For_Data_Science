# -*- coding: utf-8 -*-
"""
Created on Sun Jun 04 16:41:33 2017

@author: Liyang(Leon) Guan
"""

"""
Replace missing values with a scalar value

df.my_feature.fillna( df.my_feature.mean() )
df.fillna(0)

"""

"""
Fill nans with values near them

df.fillna(method='ffill')  # fill the values forward
df.fillna(method='bfill')  # fill the values in reverse
df.fillna(limit=5)

"""

"""
Interpolate, nearest, cubic, spline 

df.interpolate(method='polynomial', order=2)

"""
 

"""
Dropping Data

df = df.dropna(axis=0)  # remove any row with nans
df = df.dropna(axis=1)  # remove any column with nans

# Drop any row that has at least 4 NON-NaNs within it:
df = df.dropna(axis=0, thresh=4)

"""

"""
Remove duplicates

df = df.drop_duplicates(subset=['Feature_1', 'Feature_2'])

df = df.reset_index(drop=True) #reset indexes

df = df.dropna(axis=0, thresh=2).drop(labels=['ColA', axis=1]).drop_duplicates(subset=['ColB', 'ColC']).reset_index()

# inplace=True to not return a new df but modify this df.
"""

"""
Converting Data Types

>>> df.Date = pd.to_datetime(df.Date, errors='coerce')
>>> df.Height = pd.to_numeric(df.Height, errors='coerce')
>>> df.Weight = pd.to_numeric(df.Weight, errors='coerce')
>>> df.Age = pd.to_numeric(df.Age, errors='coerce')
>>> df.dtypes

"""

"""
Unique values of a series in df

df.Age.unique()
df.Age.value_counts()

"""



