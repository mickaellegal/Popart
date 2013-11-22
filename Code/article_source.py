# Import libraries
from collections import Counter
import operator


#Create a list to append the urls
source_list = []

for i, t in enumerate(db_collection_tweets.find({'html': {'$exists' : True}})):
    if t['user']['screen_name'] == 'topreads':
        to_parse = t['full_url']
        http = 'http://'
        https = 'https://'
        if http in to_parse:
            parsed = to_parse.split(http)[1].split("/")[0].strip()
            source_list.append(parsed)
            #print i,parsed
        elif https in to_parse:
            parsed = to_parse.split(https)[1].split("/")[0].strip()
            source_list.append(parsed)
            #print i,parsed
        else:
            print "Careful with this one" + to_parse


source_dict = {}
# Counting the number of occurence of each word 
for (k,v) in Counter(source_list).iteritems():
    source_dict[k] = v

# Sorting the words by number of occurences
sorted_x = sorted(source_dict.iteritems(), key=operator.itemgetter(1))
