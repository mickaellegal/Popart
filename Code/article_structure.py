

## WEBSCRAPPING/EXTRACTION/PARSING TOOLS ##
from nltk.tokenize import sent_tokenize, word_tokenize
from bs4 import BeautifulSoup
from collections import defaultdict

## CONNECTING THE DATA TO THE DATABASE ##
from pymongo import MongoClient


# Get mongoDB collection
client = MongoClient()
db = client.twitter
collection = db.tweets
db_collection_tweets = db['tweets']


# Structure of the article
for articles in db_collection_tweets.find({'content': {'$exists': True}, 'Tags': {'$exists': False} } ):
    soup = BeautifulSoup(articles['html'])
    occurrences = defaultdict(int)

    for tag in soup.findAll():
        occurrences[tag.name] += 1
    db_collection_tweets.update({ '_id' : articles['_id'] }, { '$set' : { 'Tags': occurrences} } )


# Length of the whole article
from nltk.tokenize import sent_tokenize, word_tokenize
import pdb

for articles in db_collection_tweets.find({'content': {'$exists': True}, 'Article Length': {'$exists': False}} ):
    # Length of the whole article
    sentences = sent_tokenize("".join(articles['content']))
    
    article_words = []
    for sent in sentences:
        article_words.extend(word_tokenize(sent))

    # Length of the paragraphs    
    soup = BeautifulSoup(articles['html'])    
    
    len_paragraph = []
    for p in soup.findAll('p', text=True):
        text = p.get_text()
        sentences = sent_tokenize("".join(text))
    
        words = []
        for sent in sentences:
            words.extend(word_tokenize(sent))
            len_paragraph.append(len(words))    
        
    article_length = len(article_words)
    total_paragraph = len(len_paragraph)
    if total_paragraph != 0:
        average_paragraph_length = round(float(len(article_words))/len(len_paragraph))
    else:
        average_paragraph_length = 'None'
    #print article_length, total_paragraph, average_paragraph_length
    db_collection_tweets.update({ '_id' : articles['_id'] }, { '$set' : { 'Article Length': article_length, 'Total Paragraphs': total_paragraph, 'Average Paragraph Length' : average_paragraph_length} } )     