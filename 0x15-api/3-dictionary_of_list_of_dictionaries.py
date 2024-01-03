#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"

    data = {}
    for i in range(10):
        user_id = i + 1
        users = requests.get(url + "/users/?id={}".format(user_id))
        todos = requests.get(url + "/todos?userId={}".format(user_id))
        USERNAME = users.json()[0].get('username')
        temp = [{"task": t.get("title"), "completed": t.get("completed"),
                 "username": USERNAME} for t in todos.json()]
        data[user_id] = temp

    with open("todo_all_employees.json", mode="w") as file:
        json.dump(data, file)
