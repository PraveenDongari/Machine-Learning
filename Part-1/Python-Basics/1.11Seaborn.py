# Seaborn

# importing the library

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



# seaborn has some build-in datasets

# total bil vs tip dataset



tips=sns.load_dataset('build-in datasets like tips') #import.s as pandas datasets
tips.head()


# setting a theme for the plots

sns.set_theme() # graph with grids and more spaced

# visualize the data

sns.relplot(data=tips,x='column name like total_bill',y='column name like tip',hue='smoke',style='smoker',size='size')




# load the iris dataset


iris=sns.load_dataset('iris')
iris.head()

# scatter plot

sns.scatterplot(x='sepal_length',y='petal_length',hue='species',data=iris)



# loading the titanic dataset


titanic=sns.load_dataset('titanic')
titanic.head()
titanic.shape

# count plot

sns.countplot(x='class',data=titanic)
sns.countplot(x='survive',data=titanic)

# bar-chart

sns.barplot(x='sex',y='survived',hue='class',data=titanic) # hue=> based on this. it will classify.



# house price dataset.(it is not in seaborn.it is in sklearn)


from sklearn.datasets import load_boston
house_boston=load_boston # (not in the format of pandas DataFrame.It is in the numpy array format)
house=pd.DataFrame(house_boston.data,columns=house_boston.feature_names)

print(house_boston)

house['PRICE']=house_boston.target # create the column from the numpy array

house.head()

# Distribution plot

sns.displot(house['PRICE'])


sns.distplot(house['PRICE']) # graph with curve



# correlatio (+ve correlation,-ve correlation)

# Heat map

correlation=house.corr()

# constructing a Heat map

plt.figure(figsize=(10,10))
sns.heatmap(correlation,cbar=True,fmt='.1f',annot=True,annot_kws={'size':8},cmap='Blues')