#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com"
    users = requests.get(url + "/users/?id={}".format(user_id))
    todos = requests.get(url + "/todos?userId={}".format(user_id))
    USERNAME = users.json()[0].get('username')
    data = [{"task": t.get("title"), "completed": t.get("completed"),
            "username": USERNAME} for t in todos.json()]

    with open("{}.json".format(user_id), mode="w") as file:
        json.dump({user_id: data}, file)
