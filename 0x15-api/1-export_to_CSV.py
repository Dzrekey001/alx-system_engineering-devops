#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""
import requests
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com"
    users = requests.get(url + "/users/?id={}".format(user_id))
    todos = requests.get(url + "/todos?userId={}".format(user_id))
    USERNAME = users.json()[0].get('username')

    with open("{}.csv".format(user_id), mode="w") as file:
        for task in todos.json():
            file.write('"{}","{}","{}","{}"\n'
                       .format(user_id, USERNAME, task.get("completed"),
                               task.get("title")))
