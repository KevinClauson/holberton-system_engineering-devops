#!/usr/bin/python3
"""
uses https://jsonplaceholder.typicode.com api to query info
export data in csv format
"""
import json
import requests
import sys


def my_app(root, user_url):
    """
    requests info from api
    writes to csv
    """
    all_data = {}
    users = requests.get(user_url).json()
    for u in users:
        num = str(u.get('id'))
        username = u.get('username')
        url = '{}{}{}'.format(root, '/todos/?userId=', num)
        todo = requests.get(url).json()
        all_task = []
        for to in todo:
            all_task.append({'task': to.get('title'),
                             'completed': to.get('completed'),
                             'username': username})
        all_data[num] = all_task
    file_name = "todo_all_employees.json"
    with open(file_name, 'w') as jsonfile:
        jsonfile.write(json.dumps(all_data, sort_keys=True))

if __name__ == '__main__':
    """
    APP
    """
    root = 'https://jsonplaceholder.typicode.com'
    user_url = 'https://jsonplaceholder.typicode.com/users/'
    my_app(root, user_url)
