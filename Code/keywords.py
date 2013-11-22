import string
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize


for articles in db_collection_tweets.find({'Title': {'$exists': True}}).limit(20):
    text = articles['Title'].encode('ascii', 'ignore')
    
    sentences = sent_tokenize("".join(text))
    
    words = []
    
    for sent in sentences:
        words.extend(word_tokenize(sent))
    
    
    # remove stop words and punctuation from word token array 
    filtered = [ word for word in words if word.lower() not in stopwords.words('english') and word.lower() not in string.punctuation ]

    db_collection_tweets.update({ '_id' : articles['_id'] }, { '$set' : { 'Keywords': filtered} } )