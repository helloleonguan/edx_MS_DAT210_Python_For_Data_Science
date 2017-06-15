# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 12:55:50 2017

@author: Liyang(Leon) Guan
"""

from sklearn.datasets import load_iris
from pandas.tools.plotting import parallel_coordinates
from pandas.tools.plotting import andrews_curves


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# Look pretty...
matplotlib.style.use('ggplot')
# If the above line throws an error, use plt.style.use('ggplot') instead

# Load up SKLearn's Iris Dataset into a Pandas Dataframe
data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names) 

df['target_names'] = [data.target_names[i] for i in data.target]

# Parallel Coordinates Start Here:
plt.figure()
parallel_coordinates(df, 'target_names')
plt.show()

# Andrews Curves Start Here:
plt.figure()
andrews_curves(df, 'target_names')
plt.show()

# correlation matrix
# df.corr()
plt.imshow(df.corr(), cmap=plt.cm.Blues, interpolation='nearest')
plt.colorbar()
tick_marks = [i for i in range(len(df.columns))]
plt.xticks(tick_marks, df.columns, rotation='vertical')
plt.yticks(tick_marks, df.columns)

plt.show()