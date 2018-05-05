#!/usr/bin/python3
'''
queries the reddit api
return number of hot posts
recursivley
'''
import requests


def count_words(subreddit, word_list, after="", my_dict=None):
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
    if my_dict is None:
        my_dict = {}
        for word in word_list:
            word = word.lower()
            my_dict[word] = my_dict.get(word, 0)

    if response.status_code >= 300:
        return None
    else:
        af = response.json().get("data").get("after")
        data = response.json().get("data").get("children")
        for hot in data:
            post = hot.get('data')
            hot_list = post.get('title').split()
            for word in hot_list:
                word = word.lower()
                if word in my_dict:
                    my_dict[word] += 1
        if af is not None:
            return count_words(subreddit, word_list, after=af, my_dict=my_dict)
        else:
            arr = sorted(my_dict, key=my_dict.get,reverse=True)
            for w in arr:
                if my_dict[w] > 0:
                    print("{}: {}".format(w, my_dict[w]))
