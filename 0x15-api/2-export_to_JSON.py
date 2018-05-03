#!/usr/bin/python3
"""
uses https://jsonplaceholder.typicode.com api to query info
export data in csv format
"""
import json
import requests
import sys


def my_app(num, root):
    """
    requests info from api
    writes to csv
    """
    employee_url = '{}{}{}'.format(root, '/users/', num)
    employee = requests.get(employee_url).json()
    todo_url = '{}{}{}'.format(root, '/todos/?userId=', num)
    todo = requests.get(todo_url).json()
    username = employee.get('username')
    all_task = []
    for to in todo:
        all_task.append({'task': to.get('title'),
                         'completed': to.get('completed'),
                         'username': username})
    file_name = "{}.json".format(num)
    user_data = {num: all_task}
    with open(file_name, 'w') as jsonfile:
        jsonfile.write(json.dumps(user_data))

if __name__ == '__main__':
    """
    APP
    """
    root = 'https://jsonplaceholder.typicode.com'
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        my_app(sys.argv[1], root)
