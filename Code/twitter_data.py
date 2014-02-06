import oauth2 as oauth
import urllib2 as urllib
import json

## TWITTER CREDENTIALS ##
access_token_key = "Your_access_token_key"
access_token_secret = "Your_access_token_secret"

consumer_key = "Your_consumer_key"
consumer_secret = "Your_consumer_secret"

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

########################################################

#import pdb
'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url, 
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data)

  return response

# def fetchsamples(last_id):
#   url = "https://api.twitter.com/1.1/statuses/user_timeline.json?include_entities=true&include_rts=true&screen_name=topreads&count=200&max_id=last_id" 
#   parameters = []
#   response = twitterreq(url, "GET", parameters)
#   pdb.set_trace()
#   for line in response:
#     return line.strip()

def fetchsamples():
  url = "https://api.twitter.com/1.1/users/search.json?q=Bill%20Simmons" 
  parameters = []
  response = twitterreq(url, "GET", parameters)
  #pdb.set_trace()
  for line in response:
    return line.strip()


data = fetchsamples()
twitter_data = json.loads(data)

list_followers = []
for i in xrange(len(twitter_data)):
	list_followers.append(twitter_data[i]['follwers_count'])

max(list)	
