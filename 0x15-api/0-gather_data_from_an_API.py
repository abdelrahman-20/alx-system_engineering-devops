#!/usr/bin/python3
"""Gather data from an API"""

import re
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    emp_id = sys.argv[1]

    user = requests.get(f"{url}/users/{emp_id}").json()

    params = {"userId": emp_id}
    todos = requests.get(f"{url}/todos", params=params).json()

    completed = [x.get("title") for x in todos if x.get("completed")]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(complete)) for complete in completed]
