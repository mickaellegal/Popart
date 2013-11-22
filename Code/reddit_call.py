import praw
import json

r = praw.Reddit(user_agent='my_cool_application')

submissions = r.get_subreddit('TrueReddit').get_top_from_all(limit=None)
data1 = []
for sub in submissions:
	data1.append(vars(sub))

for i in data1:
	i['subreddit'] = 'TrueReddit'
	i['author'] = 'None'
	i['reddit_session'] = 'None'	

submissions = r.get_subreddit('TrueReddit').get_top_from_day(limit=None)
data2 = []

for sub in submissions:
	data2.append(vars(sub))

for i in data2:
	i['subreddit'] = 'TrueReddit'
	i['author'] = 'None'
	i['reddit_session'] = 'None'

submissions = r.get_subreddit('TrueReddit').get_top_from_hour(limit=None)
data3 = []

for sub in submissions:
	data3.append(vars(sub))

for i in data3:
	i['subreddit'] = 'TrueReddit'
	i['author'] = 'None'
	i['reddit_session'] = 'None'

submissions = r.get_subreddit('TrueReddit').get_top_from_month(limit=None)
data4 = []

for sub in submissions:
	data4.append(vars(sub))

for i in data4:
	i['subreddit'] = 'TrueReddit'
	i['author'] = 'None'
	i['reddit_session'] = 'None'

submissions = r.get_subreddit('TrueReddit').get_top_from_week(limit=None)
data5 = []

for sub in submissions:
	data5.append(vars(sub))

for i in data5:
	i['subreddit'] = 'TrueReddit'
	i['author'] = 'None'
	i['reddit_session'] = 'None'

submissions = r.get_subreddit('TrueReddit').get_controversial_from_all(limit=None)
data6 = []

for sub in submissions:
	data6.append(vars(sub))

for i in data6:
	i['subreddit'] = 'TrueReddit'
	i['author'] = 'None'
	i['reddit_session'] = 'None'

submissions = r.get_subreddit('TrueReddit').get_controversial_from_day(limit=None)
data7 = []

for sub in submissions:
	data7.append(vars(sub))

for i in data7:
	i['subreddit'] = 'TrueReddit'
	i['author'] = 'None'
	i['reddit_session'] = 'None'

submissions = r.get_subreddit('TrueReddit').get_controversial_from_hour(limit=None)
data8 = []

for sub in submissions:
	data8.append(vars(sub))

for i in data8:
	i['subreddit'] = 'TrueReddit'
	i['author'] = 'None'
	i['reddit_session'] = 'None'

submissions = r.get_subreddit('TrueReddit').get_controversial_from_month(limit=None)
data9 = []

for sub in submissions:
	data9.append(vars(sub))

for i in data9:
	i['subreddit'] = 'TrueReddit'
	i['author'] = 'None'
	i['reddit_session'] = 'None'

submissions = r.get_subreddit('TrueReddit').get_controversial_from_week(limit=None)
data10 = []

for sub in submissions:
	data10.append(vars(sub))

for i in data10:
	i['subreddit'] = 'TrueReddit'
	i['author'] = 'None'
	i['reddit_session'] = 'None'

submissions = r.get_subreddit('TrueReddit').get_controversial_from_year(limit=None)
data11 = []

for sub in submissions:
	data11.append(vars(sub))

for i in data11:
	i['subreddit'] = 'TrueReddit'
	i['author'] = 'None'
	i['reddit_session'] = 'None'

submissions = r.get_subreddit('TrueReddit').get_new(limit=None)
data12 = []

for sub in submissions:
	data12.append(vars(sub))

for i in data12:
	i['subreddit'] = 'TrueReddit'
	i['author'] = 'None'
	i['reddit_session'] = 'None'

submissions = r.get_subreddit('TrueReddit').get_hot(limit=None)
data13 = []

for sub in submissions:
	data13.append(vars(sub))

for i in data13:
	i['subreddit'] = 'TrueReddit'
	i['author'] = 'None'
	i['reddit_session'] = 'None'

#################################################################


# submissions = r.get_subreddit('TrueReddit').get_top_from_all(limit=None)
# data1 = []

# submissions = r.get_subreddit('TrueReddit').get_top_from_day(limit=None)
# data2 = []

# submissions = r.get_subreddit('TrueReddit').get_top_from_hour(limit=None)
# data3 = []

# submissions = r.get_subreddit('TrueReddit').get_top_from_month(limit=None)
# data4 = []

# submissions = r.get_subreddit('TrueReddit').get_top_from_week(limit=None)
# data5 = []

# submissions = r.get_subreddit('TrueReddit').get_controversial_from_all(limit=None)
# data6 = []

# submissions = r.get_subreddit('TrueReddit').get_controversial_from_day(limit=None)
# data7 = []

# submissions = r.get_subreddit('TrueReddit').get_controversial_from_hour(limit=None)
# data8 = []

# submissions = r.get_subreddit('TrueReddit').get_controversial_from_month(limit=None)
# data9 = []

# submissions = r.get_subreddit('TrueReddit').get_controversial_from_week(limit=None)
# data10 = []

# submissions = r.get_subreddit('TrueReddit').get_controversial_from_year(limit=None)
# data11 = []

# submissions = r.get_subreddit('TrueReddit').get_new(limit=None)
# data12 = []

# submissions = r.get_subreddit('TrueReddit').get_hot(limit=None)
# data13 = []

title = []
true_reddit = []

list_data = [data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11,data12,data13]

for j in list_data:
	for i in j:
		if i['title'] not in title:
			true_reddit.append(i)
			title.append(i['title'])

print len(true_reddit)

with open('data.txt', 'w') as f:
    json.dump(true_reddit, f, indent=4)

