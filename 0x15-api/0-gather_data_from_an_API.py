#!/usr/bin/python3
"""
uses https://jsonplaceholder.typicode.com api to query info
"""
import requests
import sys


def my_app(num, root):
    """
    requests info from api
    """
    employee_url = '{}{}{}'.format(root, '/users/', num)
    employee = requests.get(employee_url).json()
    todo_url = '{}{}{}'.format(root, '/todos/?userId=', num)
    todo = requests.get(todo_url).json()
    completed_tasks = []
    for i in todo:
        if i.get('completed'):
            completed_tasks.append(i.get('title'))
    print("Employee {} is done with tasks({}/{}):".format(
        employee.get('name'), len(completed_tasks), len(todo)))
    for i in completed_tasks:
        print("\t {}".format(i))


if __name__ == '__main__':
    """
    APP
    """
    root = 'https://jsonplaceholder.typicode.com'
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        my_app(sys.argv[1], root)
