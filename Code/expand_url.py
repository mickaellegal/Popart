import httplib
import urlparse

def unshorten_url(url):
    parsed = urlparse.urlparse(url)
    h = httplib.HTTPConnection(parsed.netloc)
    h.request('HEAD', parsed.path)
    response = h.getresponse()
    if response.status/100 == 3 and response.getheader('Location'):
        return response.getheader('Location')
    else:
        return url

##############################
## EXPAND FOR BITLY URLS 	##
##############################


# bitly_list = []
# normal_list = []
# for i, t in enumerate(db_collection_tweets.find({'html': {'$exists' : True}})):
#     if t['user']['screen_name'] == 'topreads':
#         bit_url = 'bit.ly'
#         if bit_url in t['entities']['urls'][0]['expanded_url']:
#             #bitly_list.append(t['entities']['urls'][0]['expanded_url'])
#             burl = unshorten_url(t['entities']['urls'][0]['expanded_url'])
#             db_collection_tweets.update({ '_id' : t['_id'] }, { '$set' : { 'full_url' : burl} } )
#         else:
#             #normal_list.append(t['entities']['urls'][0]['expanded_url'])
#             nurl = t['entities']['urls'][0]['expanded_url'] 
#             db_collection_tweets.update({ '_id' : t['_id'] }, { '$set' : { 'full_url' : nurl} } )


##############################
## EXPAND FOR IFFT URLS 	##
##############################


# for t in db_collection_tweets.find({'html': {'$exists' : True}}):
#     if t['user']['screen_name'] == 'topreads':
#         ifttt_url = 'ift.tt'
#         if ifttt_url in t['entities']['urls'][0]['expanded_url']:
#             ifurl = unshorten_url(t['entities']['urls'][0]['expanded_url'])
#             db_collection_tweets.update({ '_id' : t['_id'] }, { '$set' : { 'full_url' : ifurl} } )