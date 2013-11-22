import requests
import json
import time
import sys

user_pass_dict = {'user': 'mickaellegal',
              'passwd': 'LXh3jseUsg2bBXRnw',
              'api_type': 'json'}
s = requests.Session()
s.headers.update({'User-Agent' : 'short_description_of_yourself user:your_user_name'})
r = s.post(r'http://www.reddit.com/api/login', data=user_pass_dict)
j = json.loads(r.content)
after = "t3_1q0gsd" # Set this to a T3 object to start at a specific point or leave blank to start with the most recent submissions

while True:
    time.sleep(1) # Sleep for one second to avoid going over API limits
    url = "http://www.reddit.com/r/all/new/.json?limit=100&after=" + after
    #url = "http://www.reddit.com/r/worldnews/json?limit=25&after=" + after
    html = s.get(url) # Make request to Reddit API
    if html.status_code != 200:  # This error handing is extremely basic.  Please improve.
        # Error handing block
        sys.stderr.write(str(html.status_code)) # Print HTTP error status code to STDOUT
        sys.stderr.write(url)
        continue
        # End Error handling block
    data = html.content # Print the JSON object 
    
    #after = decode['data']['after']  # Update after variable to receive the next batch of submissions in this loop 