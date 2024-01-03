#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""
import requests
from sys import argv

user_id = argv[1]
url = "https://jsonplaceholder.typicode.com"
users = requests.get(url + "/users/?id={}".format(user_id))
todos = requests.get(url + "/todos?userId={}".format(user_id))

TASK_DONE = [n for n in todos.json() if n['completed']]
NUMBER_OF_DONE_TASKS = len(TASK_DONE)
TOTAL_NUMBER_OF_TASKS = len(todos.json())

USERNAME = users.json()[0].get('name')

print("Employee {} is done with tasks ({}/{}):"
      .format(USERNAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

for task in TASK_DONE:
    print("\t {}".format(task.get("title")))
