#!/usr/bin/python3
'''
queries the reddit api
return number of hot posts
recursivley
'''
import requests


def recurse(subreddit, hot_list=[], after=""):
    '''
    api call with subreddit lookup
    '''
    root = 'https://www.reddit.com'
    path = '/r/{}/hot.json'.format(subreddit)
    url = '{}{}'.format(root, path)
    header = {'User-Agent': 'Chrome/2602:301:772d:c490:ec20:8e49:3647:8db6'}
    payload = {'count': 0, 'after': after}
    response = requests.get(url, headers=header, params=payload,
                            allow_redirects=False)
    if response.status_code >= 300:
        return None
    else:
        af = response.json().get("data").get("after")
        data = response.json().get("data").get("children")
        for hot in data:
            post = hot.get('data')
            hot_list.append(post.get('title'))
        if af is not None:
            return recurse(subreddit, hot_list=hot_list, after=af)
        else:
            return(hot_list)
