# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 16:34:27 2017

@author: Liyang(Leon) Guan
"""

"""
>>> from sklearn.decomposition import PCA
>>> pca = PCA(n_components=2, svd_solver='full')
>>> pca.fit(df)
PCA(copy=True, n_components=2, whiten=False)

>>> T = pca.transform(df)

>>> df.shape
(430, 6) # 430 Student survey responses, 6 questions..

>>> T.shape
(430, 2) # 430 Student survey responses, 2 principal components..
"""