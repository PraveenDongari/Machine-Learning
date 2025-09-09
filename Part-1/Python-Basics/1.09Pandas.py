# Pandas Library

'''

Pandas DataFrame is 2-dimensional tabular data structure with labeled axes(rows and columns)

'''

import pandas as pd



from sklearn.datasets import load_boston # => dataset that we need to import

boston_dataset=load_boston() # normal dataset
type(boston_dataset) # Pandas DataFrame
print(boston_dataset) # it is not in the structured format.so we use Pandas.



# Pandas DataFrame

boston_df=pd.DataFrame(boston_dataset.data,columns=boston_dataset.feature_names)
boston_df.head() # print 1st five data rows.

boston_df.shape # (no.of rows,no.of columns)



# importing the data from csv file to a pandas Dataframe


diabetes_df=pd.read_csv('Path of the file')
type(diabetes_df) # pandas DataFrame
diabetes_df.head() # prints first 5 rows in the python DataFrame.
diabetes_df.shape # (no.of rows,no.of cols)


# importing the data from Excel file to a Pandas DataFrame


diabetes_df=pd.read_excel('file path')


# Exporting a DataFrame to a csv file.

boston_df.to_csv('file with csv extension')


# Exporting a DataFrame to a Excel file

boston_df.to_excel('file name')


# create a DataFrame with random values

random_df=pd.DataFrame(np.random.rand(20,10)) # 20 rows and 10 cols.0<=random value <1
random_df.shape


# printing last five rows in a pandas DataFrame

boston_df.tail()


# Information of a DataFrame

boston_df.info()


# finding the number of missing values in DataFrame

boston_df.isnull().sum()





# counting the values based on the tables

diabetes_df.value_counts('column-name')


# group the values based on their mean

diabetes_df.groupby('column-name').mean()


# Statistical measures


# count or number of values

boston_df.count()

# mean value -column wise

boston_df.mean()

# standard deviation -column values

boston_df.std()

# min value -column wise

boston_df.min()

# max value for all the columns

boston_df.max()


# all the statistical measures about the DataFrame

boston_df.describe()



# Manipulating a DataFrame



# adding a column

boston_df['column-name']=boston_dataset.target # data set
boston_df.head()

# removing a perticular row=axis=0,column=axis=1

boston_df.drop(index=0,axis=0)
boston_df.drop(columns='column-name',axis=1)

# locate perticular row using index value

boston_df.iloc[2]

# locate a perticular column

print(boston_df.iloc[:,0]) # first column(index=0)
print(boston_df.iloc[:,-1]) # last column



# +ve correlation(both the variables increases or decreases) and -ve correlation(if one increases other will decreases)

'''relation between the columns'''

boston_df.corr()
