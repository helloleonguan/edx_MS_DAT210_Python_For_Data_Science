# -*- coding: utf-8 -*-
"""
Created on Sun Jun 04 15:55:58 2017

@author: Liyang(Leon) Guan
"""
import pandas as pd

# for categorical data that is ordinal 
ordered_satisfaction = ['Very Unhappy', 'Unhappy', 'Neutral', 'Happy', 'Very Happy']
df = pd.DataFrame({'satisfaction':['Mad', 'Happy', 'Unhappy', 'Neutral']})

df.satisfaction = df.satisfaction.astype("category",
    ordered=True,
    categories=ordered_satisfaction
).cat.codes

print df

# for categorical data that is nominal 
df = pd.DataFrame({'vertebrates':[
    'Bird',
    'Bird',
    'Mammal',
    'Fish',
    'Amphibian',
    'Reptile',
    'Mammal',
]})

# Method 1) map to numbers according to alphabetical order
df['vertebrates'] = df.vertebrates.astype("category").cat.codes

print df

# Method 2) binary table representation
df = pd.get_dummies(df,columns=['vertebrates'])

print df


"""
For textual data
"""

from sklearn.feature_extraction.text import CountVectorizer

corpus = [
    "Authman ran faster than Harry because he is an athlete.",
    "Authman and Harry ran faster and faster.",
]

bow = CountVectorizer()
X = bow.fit_transform(corpus) # Sparse Matrix

print bow.get_feature_names()

print X.toarray()

"""
For images
"""

"""
# Uses the Image module (PIL)
from scipy import misc

# Load the image up
img = misc.imread('image.png')

# Is the image too big? Resample it down by an order of magnitude
img = img[::2, ::2]

# Scale colors from (0-255) to (0-1), then reshape to 1D array per pixel, e.g. grayscale
# If you had color images and wanted to preserve all color channels, use .reshape(-1,3)
X = (img / 255.0).reshape(-1)

# To-Do: Machine Learning with X!
#

# Uses the Image module (PIL)
from scipy import misc

# Load the image up
dset = []
for fname in files:
  img = misc.imread(fname)
  dset.append(  (img[::2, ::2] / 255.0).reshape(-1)  )

dset = pd.DataFrame( dset )


"""

"""
For audio data
"""

"""
import scipy.io.wavfile as wavfile

sample_rate, audio_data = wavfile.read('sound.wav')
print audio_data
"""