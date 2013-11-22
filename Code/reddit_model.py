# Importing libraries
import pandas as pd
import numpy as np

# Scikit Learn Libraries
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.spatial.distance import pdist, squareform

# NLTK
from nltk.corpus import stopwords

## CONNECTING THE DATA TO THE DATABASE ##
from pymongo import MongoClient
from pymongo import errors
client = MongoClient()
db = client.project

# get mongoDB collection
collection = db.reddit

-------------------------
# Training set
-------------------------

train_art_len = []
train_avg_para_len = []
train_category = []
train_num_links = []
train_sentiment = []
train_polarity = []
train_domain = []
train_subtopic = []
train_total_para = []
train_date = []
train_tags = []
train_label = []
train_week = []

for articles in collection.find({'Model': 'Train', 'Time_Frame': 'Early'}):
    # Article Length
    train_art_len.append(int(articles['Article Length']))
    # Category 
    train_category.append(int(articles['Num_category']))
    # Label
    train_label.append(int(articles['binary_label']))
    # Subtopic
    train_subtopic.append(int(articles['Num_subtopic']))
    # Number of links
    train_num_links.append(int(len(articles['Links'])))
    # Sentiment
    train_sentiment.append(float(articles['Sentiment'][0]))
    # Polarity
    train_polarity.append(float(articles['Sentiment'][1]))
    # Domain
    train_domain.append(int(articles['Num_domain']))
    # Number of paragraph
    train_total_para.append(int(articles['Total Paragraphs']))
    # Date 
    train_date.append(articles['created_utc'])
    # Week
    train_week.append(int(articles['Week']))
    
# Creating a dataframe with the training set
train_data = pd.DataFrame({ 'date' : train_date,
                    'article_length' : train_art_len,
                    'category' : train_category,
                    'subtopic' : train_subtopic,
                    'num_links' : train_num_links,
                    'sentiment' : train_sentiment,
                    'polarity' : train_polarity,
                    'domain' : train_domain,
                    'week': train_week,
                    '1.label' : train_label}) 

-------------------------
# Test set
-------------------------

test_art_len = []
test_avg_para_len = []
test_category = []
test_num_links = []
test_sentiment = []
test_polarity = []
test_domain = []
test_subtopic = []
test_total_para = []
test_date = []
test_tags = []
test_label = []
test_week = []

for articles in collection.find({'Model': 'Test', 'Time_Frame': 'Early'}):
    # Article Length
    test_art_len.append(int(articles['Article Length']))
    # Category 
    test_category.append(int(articles['Num_category']))
    # Label
    test_label.append(int(articles['binary_label']))
    # Subtopic
    test_subtopic.append(int(articles['Num_subtopic']))
    # Number of links
    test_num_links.append(int(len(articles['Links'])))
    # Sentiment
    test_sentiment.append(float(articles['Sentiment'][0]))
    # Polarity
    test_polarity.append(float(articles['Sentiment'][1]))
    # Domain
    test_domain.append(int(articles['Num_domain']))
    # Number of paragraph
    test_total_para.append(int(articles['Total Paragraphs']))
    # Date 
    test_date.append(articles['created_utc'])
    # Week
    test_week.append(int(articles['Week']))
    

test_data = pd.DataFrame({ 'date' : test_date,
                    'article_length' : test_art_len,
                    'category' : test_category,
                    'subtopic' : test_subtopic,
                    'num_links' : test_num_links,
                    'sentiment' : test_sentiment,
                    'polarity' : test_polarity,
                    'domain' : test_domain,
                    'week': test_week,
                    '1.label' : test_label})

-------------------------
# Random Forests
-------------------------

# Import the random forest package
from sklearn.ensemble import RandomForestClassifier 

# Create the random forest object which will include all the parameters
# for the fit
Forest = RandomForestClassifier(n_estimators = 1000)

# Fit the training data to the training output and create the decision
# trees
Forest = Forest.fit(train_data.iloc[:,1:9],train_data.iloc[:,0:1])

# Take the same decision trees and run on the test data
Output = Forest.predict(test_data.iloc[:,1:9])

Accuracy = Forest.score(test_data.iloc[:,1:9],test_data.iloc[:,0:1])

print Forest.score(train_data.iloc[:,1:9],train_data.iloc[:,0:1])
print Accuracy

-------------------------
# Main Features
-------------------------

importances = Forest.feature_importances_

indices = np.argsort(importances)[::-1]

# Print the feature ranking
print("Feature ranking:")

for f in range(8):
    print("%d. feature %d (%f)" % (f + 1, indices[f], importances[indices[f]]))

-------------------------
# Model Accuracy
-------------------------

y_true = np.array(test_data.iloc[:,0:1])
y_pred = np.array(Output)

# Calculating the precision of the model
from sklearn.metrics import precision_score

print precision_score(test_data.iloc[:,0:1], Output)

# Calculating the recall of the model
from sklearn.metrics import recall_score

print recall_score(test_data.iloc[:,0:1], Output)

# Classification report
from sklearn.metrics import classification_report
target_names = ['class 0', 'class 1']

print(classification_report(y_true, y_pred, target_names=target_names))
