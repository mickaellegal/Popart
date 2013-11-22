# This script will collect and update the MongoDB tweets database 
# Importing the libraries
# Alchemy API
from __future__ import print_function
from alchemyapi import AlchemyAPI

import requests
import oauth2 as oauth
import urllib2 as urllib
import json
import time

## WEBSCRAPPING/EXTRACTION/PARSING TOOLS ##
import nltk
from dateutil import parser
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
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

# Get Alchemy API
alchemyapi = AlchemyAPI()

## GETTING ALL THE FEATURES ONE BY ONE ##

# We first open the file with all the links and append them to a list

# GETTING THE TITLE, THE DESCRIPTION OF THE ARTICLE, THE IMAGE

# for articles in db_collection_tweets.find({'full_url': {'$exists' : True}, 'Title': {'$exists' : False} }):
# 	urls = articles['full_url'] 
# 	try:
# 		html = requests.get(urls, timeout = 6).text
	
# 		extracted = extraction.Extractor().extract(html, source_url=urls)
			

# 		db_collection_tweets.update({ '_id' : articles['_id'] }, { '$set' : { 'Title' : extracted.title, 'Description': extracted.description, 'Image': extracted.image } } )
	
# 	except AttributeError:
# 		pass

# 	except requests.ConnectionError:
# 		pass
			
# 	except requests.exceptions.Timeout:
# 		pass
	

# GETTING THE AUTHOR OF THE ARTICLE

# for articles in db_collection_tweets.find({'full_url': {'$exists' : True}, 'Author': {'$exists' :False}}):
# 	urls = articles['full_url']
# 	try: 
# 		response = alchemyapi.author('url',urls)
	
# 		db_collection_tweets.update({ '_id' : articles['_id'] }, { '$set' : { 'Author':response['author'] } } )

		
# 	except KeyError:
# 		continue	
# print('author: ', response['author'])

# GETTING THE TEXT OF THE ARTICLE
	
# for articles in db_collection_tweets.find({'full_url': {'$exists' : True}}):
# 	urls = articles['full_url']
	
# 	try:
# 		extractor = Extractor(extractor='ArticleExtractor', url=urls)
# 		text = extractor.getText()
# 		db_collection_tweets.update({ '_id' : articles['_id'] }, { '$set' : { 'content' : text} } )

# 	except AttributeError:
# 		pass

# 	except requests.ConnectionError:
# 		pass
			
# 	except requests.exceptions.Timeout:
# 		pass	


# Extract page text from a web URL (ignoring navigation links, ads, etc.).

URL='http://readwrite.com/2013/10/25/neural-processing-unit#awesm=~olxve0AzIh9AHZ'

from httplib import BadStatusLine

try:
	extractor = Extractor(extractor='ArticleExtractor', url=URL)
	extracted_text = extractor.getText()
	print(extracted_text)
    # do something with page
except BadStatusLine:
    print("could not fetch %s" % urls)


