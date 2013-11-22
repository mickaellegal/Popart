# from textblob import TextBlob
from text.classifiers import NaiveBayesClassifier
from collections import Counter

train = [
    ('international news features analysis from Africa Asia-Pacific Europe Latin America Middle East South Asia China.', 'World'),
    ('world country global breaking news features analysis current affairs.', 'World'),
    ('war non-stop coverage conflicts scandals uprisings everyday life.', 'World'),
    ('borders foreign China France U.K', 'World'),
    ('technology developments hardware software networking Apple iPad Windows Samsung.', 'Technology'),
    ("tech and multimedia Internet telecommunications wireless applications electronics computers email Web", 'Technology'),
    ('innovation acquisitions startups trends products tech hacker', 'Technology'),
    ('gadgets prototypes future social media Microsoft iPhone.', 'Technology'),
    ("Opinion analysis American global politics elections Iraq North Korea White House", 'Politics'),
    ('political parties political campaigns national politics Congress Capitol Hill lobbying advocacy bill law', 'Politics'),
    ('administration subsidized insurance law bans state.', 'Politics'),
    ('higher court justice crime governor', 'Politics'),
    ('business and financial on U.S. international companies.', 'Business'),
    ('small business business financial personal finance trends stock market index stock data stock market news.', 'Business'),
    ("economic news stock futures stock quotes & personal finance advice marketing partnerships", 'Business'),
    ('business Wall Street media advertising international business banking interest rates stock market currencies & funds.', 'Business'),
    ('NFL football MLB baseball NBA basketball NHL hockey college basketball and football', 'Sport'),
    ("sports scores in-depth player and team schedules fantasy games standings NFL MLB NBA NHL and NCAA sports", 'Sport'),
    ('sports news on the NFL the NBA the NCAA the NHL baseball golf tennis soccer the World Series Super Bowl the Olympics', 'Sport'),
    ('NFL MLB NBA NHL MMA college football and basketball NASCAR fantasy sports', 'Sport'),
    ('global warming extrasolar planets stem cells bird flu autism nano dinosaurs evolution.', 'Science'),
    ('wormholes outer space engineering humans smartest animal far-Off Planets Like the Earth Dot the Galaxy.', 'Science'),
    ('Science demystifies natural engineering space military physics, dreams supernatural phenomena.', 'Science'),
    ("microbe mammal origins evolution life forms. Explore biology genetics evolution", 'Science'),
    ('art news exhibitions events artists galleries museums editions books mapping the art.', 'Art'),
    ('art daily art Museums Exhibits Artists Milestones Digital Art Architecture', 'Art'),
    ("exhibitions interesting random weirdness photography painting prints design sculpture.", 'Art'),
    ('artists galleries museums and auction houses movies documentary.', 'Art'),
    ('Medicine, Health, Drugs, drugs fitness nutrition health care mental health drugs diet pregnancy babies cancer AIDS allergies & asthma.', 'Health'),
    ('Drugs supplements living healthy family pregnancy, energizing moves recipes losing weight feeling great.', 'Health'),
    ('Weight Loss & Diet Plans Food & Recipes Fitness & Exercise Beauty Balance & Love Sex & Relationships Oral Care yoga Aging Well.', 'Health'),
    ('Conceive Parenting Newborn & Baby Children Vaccines Raising Fit Kids Pets.', 'Health')
]
## CREATING THE CLASSIFIER ##
cl = NaiveBayesClassifier(train)

for articles in db_collection_tweets.find({'content': {'$exists': True}}):
    #print articles['full_url']
    category = cl.classify(articles['content'])
    db_collection_tweets.update({ '_id' : articles['_id'] }, { '$set' : { 'Category': category} } )

## DISTRIBUTION OF THE CATEGORIES IN THE SAMPLE ##

# Listing all the categories
list_cat = []
for articles in db_collection_tweets.find({'Category': {'$exists' : True}}):
    list_cat.append(articles['Category'])    

# Counting the number of occurences of each category
cat_dict = {}
for (k,v) in Counter(list_cat).iteritems():
    cat_dict[k] = v

'''
{u'Art': 178,
 u'Business': 857,
 u'Health': 64,
 u'Politics': 268,
 u'Science': 83,
 u'Sport': 161,
 u'Technology': 402,
 u'World': 512}
'''