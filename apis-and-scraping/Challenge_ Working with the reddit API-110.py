## 2. Authenticating with the API ##

headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
response = requests.get("https://oauth.reddit.com/r/python/top", headers = headers,
                       params = {"t": "day"})
python_top = response.json()

## 3. Getting the Most Upvoted Post ##

print(type(python_top), len(python_top), python_top.keys())
print(python_top['kind'])
print(type(python_top['data']), len(python_top['data']), python_top['data'].keys())
print(type(python_top['data']['children']), len(python_top['data']['children']))

python_top_articles = python_top['data']['children']
most_ups = 0
most_upvoted = ""
for article in python_top_articles:
    if article['data']['ups'] > most_ups:
        most_ups = article['data']['ups']
        most_upvoted = article['data']['id']

## 4. Getting Post Comments ##

url = "https://oauth.reddit.com/r/python/comments/" + most_upvoted
response = requests.get(url, headers = headers)
comments = response.json()

## 5. Getting the Most Upvoted Comment ##

comments_list = comments[1]['data']['children']

most_ups = 0
most_upvoted_comment = ""
for comment in comments_list:
    if comment['data']['ups'] > most_ups:
        most_ups = comment['data']['ups']
        most_upvoted_comment = comment['data']['id']


## 6. Upvoting a Comment ##

payload = {'dir':1, 'id':most_upvoted_comment}
headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
response = requests.post("https://oauth.reddit.com/api/vote", 
                         json = payload,
                        headers = headers)
status = response.status_code