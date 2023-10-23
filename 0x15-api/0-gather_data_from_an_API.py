#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID,
returns information about his/her todo list progress. """
import requests
from sys import argv


if __name__ == "__main__":
    """ """

    url = "https://jsonplaceholder.typicode.com"
    todo_list = requests.get(url + "/user/{}/todos".format(argv[1])).json()
    user = (requests.get(url + "/users/{}".format(argv[1])).json().get("name"))

    titles = []
    counter = 0
    for todo in todo_list:
        if todo.get("completed"):
            counter += 1
            titles.append(todo.get("title"))

    print("Employee {} is done with tasks({}/{}):"
          .format(user, counter, len(todo_list)))
    for title in titles:
        print("\t {}".format(title))

# if __name__ == '__main__':
#     """ """
#     base_url = 'https://jsonplaceholder.typicode.com/'
#     EMPLOYEE_NAME = requests.get(
#         '{}users/{}'.format(base_url, argv[1])).json()
#     NUMBER_OF_DONE_TASKS = requests.get(
#         '{}todos?userId={}&completed=true'.format(base_url,
#                                                   argv[1])).json()
#     TOTAL_NUMBER_OF_TASKS = requests.get(
#         '{}todos?userId={}'.format(base_url, argv[1])).json()

#     print(
#         'Employee {} is done with tasks({}/{}):'.format(
#             EMPLOYEE_NAME['name'], len(NUMBER_OF_DONE_TASKS),
#             len(TOTAL_NUMBER_OF_TASKS)))

#     for task in NUMBER_OF_DONE_TASKS:
#         print("\t {}".format(task["title"]))
