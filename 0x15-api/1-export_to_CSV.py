#!/usr/bin/python3
"""
uses https://jsonplaceholder.typicode.com api to query info
export data in csv format
"""
import csv
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
        all_task.append([to.get('completed'), to.get('title')])
    file_name = "{}.csv".format(num)
    with open(file_name, 'w') as csvfile:
        spamwriter = csv.writer(
            csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        for task in all_task:
            spamwriter.writerow([num, username, task[0], task[1]])

if __name__ == '__main__':
    """
    APP
    """
    root = 'https://jsonplaceholder.typicode.com'
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        my_app(sys.argv[1], root)
