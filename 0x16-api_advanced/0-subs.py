#!/usr/bin/python3
'''
queries the reddit api
return number of subscribers
'''
import requests


def number_of_subscribers(subreddit):
    '''
    api call with subreddit lookup
    '''
    root = 'https://www.reddit.com'
    path = '/r/{}/about.json'.format(subreddit)
    url = '{}{}'.format(root, path)
    header = {'User-Agent': 'Chrome/2602:301:772d:c490:ec20:8e49:3647:8db6'}
    response = requests.get(url, headers=header, allow_redirects=False)
    if response.status_code >= 300:
        return 0
    return response.json().get('data').get('subscribers')
