#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID,
returns information about his/her todo list progress.
"""

import requests
from sys import argv


if __name__ == "__main__":
    """ get user name and todo list progress"""

    url = "https://jsonplaceholder.typicode.com/"
    todo_list = requests.get(url + "user/{}/todos".format(argv[1])).json()
    user = (requests.get(url + "users/{}".format(argv[1])).json().get("name"))

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
