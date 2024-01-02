# ALX System Engineering & DevOps - Project 0x15-api

## Task 0: Gather data from an API

### Description
Write a Python script that, using a REST API, retrieves information about an employee's TODO list progress.

### Requirements
- The script must use the `urllib` or `requests` module.
- Accept an integer as a parameter representing the employee ID.
- Display employee TODO list progress in the specified format.

### Usage
```bash
$ python3 0-gather_data_from_an_API.py 2
```
##Task 1: Export to CSV

###Description
Extend the Python script from Task 0 to export data in CSV format.

###Requirements
- Record all tasks owned by the employee.
- Format: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
- File name: USER_ID.csv

###Usage
```bash
$ python3 1-export_to_CSV.py 2
```

##Task 2: Export to JSON

##Description
Extend the Python script from Task 0 to export data in JSON format.

###Requirements
- Record all tasks owned by the employee.
- Format: { "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
- File name: USER_ID.json

##Usage
```bash
$ python3 2-export_to_JSON.py 2
```

##Task 3: Dictionary of list of dictionaries
##Description
Extend the Python script from Task 0 to export data in a JSON format containing all tasks from all employees.

###Requirements
- Record all tasks from all employees.
- Format: { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}
- File name: todo_all_employees.json
```bash
$ python3 3-dictionary_of_list_of_dictionaries.py
```
