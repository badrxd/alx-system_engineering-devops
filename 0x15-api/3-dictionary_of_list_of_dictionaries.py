#!/usr/bin/python3
"""script to export data in the JSON format.
"""

import json
import requests


if __name__ == '__main__':
    """ """
    base_url = 'https://jsonplaceholder.typicode.com/'
    EMPLOYEE_NAME = requests.get(
        '{}users'.format(base_url)).json()

    TODOS = requests.get(
        '{}todos'.format(base_url)).json()

    with open('todo_all_employees.json', 'w', newline='') as jsonfile:
        obj = {}
        for todos in TODOS:
            i = todos.get('userId')
            dct = {}
            if i not in obj:
                obj[i] = []
            dct['username'] = EMPLOYEE_NAME[i-1].get('username')
            dct['task'] = todos.get('title')
            dct['completed'] = todos.get('completed')
            obj[i].append(dct)
        json.dump(obj, jsonfile)
