## CONNECTING THE DATA TO THE DATABASE ##
from pymongo import MongoClient
from pymongo import errors


# Get mongoDB collection
client = MongoClient()
db = client.twitter
collection = db.tweets
db_collection_tweets = db['tweets']

# Importing Textblob
from textblob import TextBlob

for articles in db_collection_tweets.find({'content': {'$exists': True}}):
    text = TextBlob(articles['content'])
    sentiment = text.sentiment
    db_collection_tweets.update({ '_id' : articles['_id'] }, { '$set' : { 'Sentiment': sentiment} } )


        