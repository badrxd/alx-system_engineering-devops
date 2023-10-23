#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID,
returns information about his/her todo list progress.
"""

import sys
import requests
from sys import argv


if __name__ == '__main__':
    """ """
    base_url = 'https://jsonplaceholder.typicode.com/'
    EMPLOYEE_NAME = requests.get(
        '{}users/{}'.format(base_url, argv[1])).json()
    NUMBER_OF_DONE_TASKS = requests.get(
        '{}todos?userId={}&completed=true'.format(base_url,
                                                  argv[1])).json()
    TOTAL_NUMBER_OF_TASKS = requests.get(
        '{}todos?userId={}'.format(base_url, argv[1])).json()

    print(
        'Employee {} is done with tasks({}/{}):'.format(
            EMPLOYEE_NAME['name'], len(NUMBER_OF_DONE_TASKS),
            len(TOTAL_NUMBER_OF_TASKS)))

    for task in NUMBER_OF_DONE_TASKS:
        print("\t {}".format(task["title"]))
