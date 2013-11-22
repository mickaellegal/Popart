# This script will collect and update the MongoDB tweets database 
# Importing the libraries

import requests
import urllib2
from httplib import BadStatusLine

## WEBSCRAPPING/EXTRACTION/PARSING TOOLS ##

# Feedparser/Boilerpipe
from boilerpipe.extract import Extractor
from bs4 import BeautifulSoup

## CONNECTING THE DATA TO THE DATABASE ##
from pymongo import MongoClient
from pymongo import errors

# Get mongoDB collection
client = MongoClient()
db = client.twitter
collection = db.tweets
db_collection_tweets = db['tweets']


## GETTING THE CONTENT OF THE ARTICLES ##

class MyException(Exception):
    pass

for articles in db_collection_tweets.find({'full_url': {'$exists' : True}, 'content': {'$exists': False}}):
    urls = articles['full_url']
    print urls
    
    try:
        html = requests.get(urls)
        # We first use Beautiful Soup to Handle the encoding/decoding issues
        soup = BeautifulSoup(html.text)
        extractor = Extractor(extractor='DefaultExtractor', html=unicode(soup))
        extracted_text = extractor.getText()
        
        db_collection_tweets.update({ '_id' : articles['_id'] }, { '$set' : { 'content': extracted_text} } )
    
    except BadStatusLine:
        print("could not fetch %s" % urls)
    
    except socket.timeout, e:
        # For Python 2.7
        raise MyException("There was an error: %r" % e)
        
    except urllib2.HTTPError, e:
        print(e.code)
        
  