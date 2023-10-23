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
    NUMBER_OF_DONE_TASKS = requests.get(
        '{}todos?userId={}&completed=true'.format(base_url,
                                                  argv[1])).json()

    with open('USER_ID.csv', 'w', newline='') as csvfile:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                      "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for task in NUMBER_OF_DONE_TASKS:
            writer.writerow({'USER_ID': argv[1],
                             'USERNAME': EMPLOYEE_NAME['name'],
                             'TASK_COMPLETED_STATUS':
                                 len(NUMBER_OF_DONE_TASKS),
                             'TASK_TITLE': task['title']})
