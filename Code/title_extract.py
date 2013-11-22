# This script will collect and update the MongoDB tweets database 
# Importing the libraries

import requests
import urllib2


## WEBSCRAPPING/EXTRACTION/PARSING TOOLS ##

# Feedparser/Boilerpipe
import feedparser
import extraction
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


## GETTING ALL THE FEATURES ONE BY ONE ##

# We first open the file with all the links and append them to a list

# GETTING THE TITLE, THE DESCRIPTION OF THE ARTICLE, THE IMAGE

for articles in db_collection_tweets.find({'full_url': {'$exists' : True}, 'Title': {'$exists' : False} }):
	urls = articles['full_url'] 
	try:
		html = requests.get(urls)
        # We first use Beautiful Soup to Handle the encoding/decoding issues
        soup = BeautifulSoup(html.text)
		
		extracted = extraction.Extractor().extract(soup, source_url=urls)
			

		db_collection_tweets.update({ '_id' : articles['_id'] }, { '$set' : { 'Title' : extracted.title, 'Description': extracted.description, 'Image': extracted.image } } )
	
	except AttributeError:
		pass

	except requests.ConnectionError:
		pass
			
	except requests.exceptions.Timeout:
		pass
	



