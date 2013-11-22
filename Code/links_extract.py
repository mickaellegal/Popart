# This script will collect and update the MongoDB tweets database 
# Importing the libraries

import requests
import urllib2
import re

## WEBSCRAPPING/EXTRACTION/PARSING TOOLS ##

# Beautiful Soup parser
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

for articles in db_collection_tweets.find({'full_url': {'$exists' : True} }):
    urls = articles['full_url']
    print urls
    
    try:
        html = requests.get(urls)
        # We first use Beautiful Soup to Handle the encoding/decoding issues
        soup = BeautifulSoup(html.text)
        
        links = []
        for a in soup.findAll('a',href=True):
            if re.findall('http', a['href']):
               links.append(a['href'])
        
        db_collection_tweets.update({ '_id' : articles['_id'] }, { '$set' : { 'Links': links} } )
    
    except BadStatusLine:
        print("could not fetch %s" % urls)
    
    except socket.timeout, e:
        # For Python 2.7
        raise MyException("There was an error: %r" % e)
        
    except urllib2.HTTPError, e:
        print(e.code)
        
 	except requests.exceptions.RequestException:
        raise MyException("There was an error: %r" % e)
        pass