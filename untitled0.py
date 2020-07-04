# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 07:51:18 2020

@author: DELL
"""

# importing pandas and numpy

import pandas as pd
import numpy as np

# creating a sample data frame

data = pd.DataFrame ({
    'age' :[ 10, 22, 13, 21, 12, 11, 17],
    'section' :[ 'A', 'B', 'C', 'B', 'B', 'A', 'A'],
    'city' : [ 'Gurgaon', 'Delhi', 'Mumbai', 'Delhi', 'Mumbai', 'Delhi', 'Mumbai'],
    'gender' : [ 'M', 'F', 'F', 'M', 'M', 'M', 'F'],
    'color' :['red', np.NAN, 'yellow', np.NAN, 'black', 'green', 'red']
    })

#view the data
data

# select all rows with a condition
data.loc[data.age>= 15]

# select data with multiple conditions
data.loc[(data.age >= 12) & (data.gender == 'M')]

#slice
data.loc[1:3]


# select few columns with a condition
data.loc[(data.age >= 12), ['city', 'gender']]

# update a column with condition
data.loc[(data.age >= 12), ['section']] = 'M'
data

# update multiple columns with condition
data.loc[(data.age >= 20), ['section', 'city']] = ['S','Pune']
data

# select rows with indexes
data.iloc[[0,2]]


# select rows with particular indexes and particular columns
data.iloc[[0,2],[1,3]]

# select a range of rows
data.iloc[1:3]

# select a range of rows and columns
data.iloc[1:3,2:4]