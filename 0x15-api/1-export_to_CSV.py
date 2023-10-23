#!/usr/bin/python3
"""script use to export data in the CSV format.
"""

import csv
import requests
from sys import argv


if __name__ == '__main__':
    """ """
    base_url = 'https://jsonplaceholder.typicode.com/'
    EMPLOYEE_NAME = requests.get(
        '{}users/{}'.format(base_url, argv[1])).json()

    TOTAL_NUMBER_OF_TASKS = requests.get(
        '{}todos?userId={}'.format(base_url, argv[1])).json()

    file = '{}.csv'.format(argv[1])
    with open(file, 'w', newline='') as csvfile:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                      "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)
        for task in TOTAL_NUMBER_OF_TASKS:
            writer.writerow({"USER_ID": argv[1],
                             'USERNAME': EMPLOYEE_NAME.get("username"),
                             'TASK_COMPLETED_STATUS': task.get('completed'),
                             'TASK_TITLE': task.get('title')})
