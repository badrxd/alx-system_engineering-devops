#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID,
returns information about his/her todo list progress.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {} <employee ID>".format(sys.argv[0]))
        sys.exit(1)

    try:
        id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        id
    )
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        id
    )

    response = requests.get(user_url)
    if response.status_code != 200:
        print("Error: Unable to fetch the user data")
        sys.exit(1)

    user = response.json()
    name = user.get("name")

    response = requests.get(todos_url)
    if response.status_code != 200:
        print("Error: Unable to fetch the todos data")
        sys.exit(1)

    todos = response.json()
    done_tasks = [task for task in todos if task.get("completed")]

    print(
        "Employee {} is done with tasks({}/{}):".format(
            name, len(done_tasks), len(todos)
        )
    )
    for task in done_tasks:
        print("\t {}".format(task.get("title")))
