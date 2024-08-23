#!/usr/bin/python3
"""Gather data from an API & Write To CSV"""

import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user_id = sys.argv[1]

    user = requests.get(f"{url}/users/{user_id}").json()
    username = user.get("username")

    params = {"userId": user_id}
    todos = requests.get(f"{url}/todos", params=params).json()

    data_to_export = {
        user_id: [
            {
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            }
            for t in todos
        ]
    }
    with open(f"{user_id}.json", "w") as fp:
        fp.write(json.dumps(data_to_export, indent=4))
