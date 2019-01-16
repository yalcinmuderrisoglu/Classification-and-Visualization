# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 21:49:30 2019

@author: YALCIN.M
"""

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv('IMDB-Movie-Data.csv')

dataset.head(3)




dataset.info()

# descriptive statistics
dataset_desc = dataset.describe()
print(dataset)

Revenue = dataset.iloc[:,10:11].values

from sklearn.preprocessing import Imputer

imputer= Imputer(missing_values='NaN', strategy = 'mean', axis=0 )    

Revenue[:,10:11] = imputer.transform(Revenue[:,10:11])
print(Revenue)

# **************** GRAFİKLER *************************
# scatter plot
plt.figure(figsize=(15,6))
plt.scatter(dataset['Rating'],dataset['Revenue (Millions)'])
plt.xlabel('RATE',color = 'red').set_size(20)
plt.ylabel('REVENUE',color = 'yellow').set_size(20)


# point plot
plt.figure(figsize=(10,8))
sns.pointplot(dataset['Rating'],dataset['Revenue (Millions)'], color='grey')
plt.xlabel('RATE').set_size(20)
plt.ylabel('REVENUE').set_size(20)

# count plot
plt.figure(figsize=(20,8))
sns.countplot(x=dataset['Rating'].round(2))
plt.xlabel('Rating').set_size(15)
plt.ylabel('Count').set_size(15)


# bar plot
plt.figure(figsize=(10,8))
sns.barplot(dataset['quality'],dataset['total sulfur dioxide'])
plt.xlabel('Quality').set_size(20)
plt.ylabel('Total Sulfur Dioxide').set_size(20)




Revenue = dataset.iloc[:,1:2].values
Metascore = dataset.iloc[:,1:2].values

imputer = imputer.fit(Yas[:,1:4])
Yas[:,1:4] = imputer.transform(Yas[:,1:4])
print(Yas)



#Revenue (Millions)    872 non-null float64
#Metascore             936 non-null float64

from sklearn.preprocessing import Imputer

imputer= Imputer(missing_values='NaN', strategy = 'mean', axis=0 )    