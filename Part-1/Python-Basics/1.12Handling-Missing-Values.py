''' Methods to Handle missing values
1)Imputation
2)Dropping

'''


# Imputation : (Recammended)


# importing the libraries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Loading the Dataset to a Pandas DataFrame


dataset=pd.read_csv('File of the path')
dataset.shape

dataset.isnull().sum() # number of missing values



''' Central Tendencies :

1)Mean : Average of elements
2)Median : Average of middle values
3)Mode : most recurring element

'''



# Analysis the distribution of data

fig,ax=plt.subplots(figsize=(8,8))
sns.displot(dataset.salary) # salary is the column in which it has missing values



# Replacing the missing values with the median value



dataset['salary'].fillna(dataset['salary'].median(),inplace=True)

dataset.isnull().sum()


# Filling with Mean Values


dataset['salary'].fillna(dataset['salary'].mean(),inplace=True) # na => not avaliable

dataset.isnull().sum()


# Filling with Mode Values

dataset['salary'].fillna(dataset['salary'].mode(),inplace=True)

dataset.isnull().sum()




# Droping : (Not-Recommended)



salary_dataset=pd.read_csv('path of csv file')

salary_dataset.shape # dimention

salary_dataset.isnull().sum() # number of missing values



# droping the missing values

salary_dataset=salary_dataset.dropna(how='any')

salary_dataset.isnull().sum() # number of missing values=0

salary_dataset.shape # dimention after deletion the data