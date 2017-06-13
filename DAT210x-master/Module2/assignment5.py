import pandas as pd
import numpy as np


#
# TODO:
# Load up the dataset, setting correct header labels.
#
# .. your code here ..
census_df = pd.read_csv("Datasets/census.data", header=None, 
            names=['education', 'age', 'capital-gain', 'race', 'capital-loss', 'hours-per-week', 'sex', 'classification'],
            index_col = 0)


#
# TODO:
# Use basic pandas commands to look through the dataset... get a
# feel for it before proceeding! Do the data-types of each column
# reflect the values you see when you look through the data using
# a text editor / spread sheet program? If you see 'object' where
# you expect to see 'int32' / 'float64', that is a good indicator
# that there is probably a string or missing value in a column.
# use `your_data_frame['your_column'].unique()` to see the unique
# values of each column and identify the rogue values. If these
# should be represented as nans, you can convert them using
# na_values when loading the dataframe.
#
# .. your code here ..
census_df.replace("?", np.nan, inplace=True)
census_df["capital-gain"] = pd.to_numeric(census_df["capital-gain"], errors='coerce')


#
# TODO:
# Look through your data and identify any potential categorical
# features. Ensure you properly encode any ordinal and nominal
# types using the methods discussed in the chapter.
#
# Be careful! Some features can be represented as either categorical
# or continuous (numerical). If you ever get confused, think to yourself
# what makes more sense generally---to represent such features with a
# continuous numeric type... or a series of categories?
#
# .. your code here ..

# ordinal - education
ordered_education = ["Preschool", "1st-4th", "5th-6th", "7th-8th", "9th", "10th", "11th",
                     "12th", "Some-college", "Bachelors", "Masters", "HS-grad", "Doctorate"]
census_df.education = census_df.education.astype("category", ordered=True, 
                                                 categories=ordered_education).cat.codes
                                                 
# ordinal - classification
ordered_classification = ["<=50K", ">50K"]
census_df.classification = census_df.classification.astype("category", ordered=True,
                                                           categories=ordered_classification).cat.codes
                                                           
# nominal - race
census_df = pd.get_dummies(census_df, columns=["race"])

# nominal - sex
census_df = pd.get_dummies(census_df, columns=["sex"])
#print sex_df

#
# TODO:
# Print out your dataframe
#
# .. your code here ..
print census_df

