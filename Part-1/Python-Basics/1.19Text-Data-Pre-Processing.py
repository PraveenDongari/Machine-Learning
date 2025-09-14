# importing the dependies

import numpy as np # importing the entire library
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords # (corpus => collection of words ,nltk => natural language tool kit)
from nltk.stem.porter import porterStemmer # importing specific functions from the entire library
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split



# stopwords like :i,me,my,we our,he,him....etc.
nltk.download('stopwords')
print(stopwords.words('english'))

# load the data to a pandas dataframe

news_data=pd.read_csv('file path')
news_data.head()
news_data.shape

# checking for missing values

news_data.isnull().sum()

# replacing missing values with null string

news_data=news_data.fillna('') # na => not available

# merging the author name ,news title and adding new column

news_data['new column name']=news_data['column name']+''+news_data['another column name']

# seperating feature and target

X=news_data.drop(columns='column name',axis=1)
Y=news_data['column-name']

print(X)
print(Y)


# Stemming : reducing a word to its keyword. Eg: enjoable =>enjoy. using porterStemmer function

port_stem=porterStemmer()

def stemming(content):
    stemmed_content=re.sub('[^a-zA-Z]' , ' ' ,content) # excluding others like 1,2,3:;./..etc
    stemmed_content=stemmed_content.lower() # uppercase to lower
    stemmed_content=stemmed_content.split()
    
    stemmed_content=[port_stem.stem(word) for word in 
                    stemmed_content if not word in stopwords.words('english')] # applying the stemming not to the stopwords.
    stemmed_content=' '.join(stemmed_content)
    return stemmed_content



news_data['content']=news_data['content'].apply(stemming)
print(news_data['content'])


X=news_data['content'].values
Y=news_data['label'].values
print(X)
print(Y)
print(Y.shape)

# converting textual data to feature vectors using TfidfTransformer.


vectorizer=TfidfTransformer()
vectorizer.fit(X)

X=vectorizer.transform(X)
print(X)

# spliting data into training data and testing data.(same as the numeric data pre processing)