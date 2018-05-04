#!/usr/bin/python3
'''
queries the reddit api
return number of subscribers
'''
import requests


def top_ten(subreddit):
    '''
    api call with subreddit lookup
    '''
    root = 'https://www.reddit.com'
    path = '/r/{}/hot.json'.format(subreddit)
    url = '{}{}'.format(root, path)
    header = {'User-Agent': 'Chrome/2602:301:772d:c490:ec20:8e49:3647:8db6'}
    parameters = {'limit': 10}
    response = requests.get(url, headers=header, params=parameters,
                            allow_redirects=False)
    if response.status_code >= 300:
        print("None")
    else:
        data = response.json().get("data").get("children")
        for hot in data:
            post = hot.get('data')
            print(post.get('title'))
