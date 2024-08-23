#!/usr/bin/python3
"""Gather data from an API & Write To CSV"""

import csv
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user_id = sys.argv[1]

    user = requests.get(f"{url}/users/{user_id}").json()
    username = user.get("username")

    params = {"userId": user_id}
    todos = requests.get(f"{url}/todos", params=params).json()

    completed = [x.get("title") for x in todos if x.get("completed")]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(complete)) for complete in completed]

    with open(f"{user_id}.csv", "w") as fp:
        writer = csv.writer(fp, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
        ) for t in todos]
