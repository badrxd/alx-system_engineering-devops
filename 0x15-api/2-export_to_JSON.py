#!/usr/bin/python3
"""script to export data in the JSON format.
"""

import json
import requests
from sys import argv


if __name__ == '__main__':
    """ """
    base_url = 'https://jsonplaceholder.typicode.com/'
    EMPLOYEE_NAME = requests.get(
        '{}users/{}'.format(base_url, argv[1])).json()

    TODOS = requests.get(
        '{}todos?userId={}'.format(base_url, argv[1])).json()

    file = '{}.json'.format(argv[1])
    with open(file, 'w', newline='') as jsonfile:
        ls = []
        obj = {}
        for todos in TODOS:
            dct = {}
            dct['task'] = todos.get('title')
            dct['completed'] = todos.get('completed')
            dct['username'] = EMPLOYEE_NAME.get('username')
            ls.append(dct)
        obj[argv[1]] = ls
        json.dump(obj, jsonfile)
