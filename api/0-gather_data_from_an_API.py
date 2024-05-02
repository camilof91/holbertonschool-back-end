#!/usr/bin/python3
"""
Using this REST API, for a given employee ID, returns information about his/her
TODO list progress
"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) != 2:
        print(f"Usage: {argv[0]} <employee_id>")
        exit(1)

    employee_id = argv[1]

    user_response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    todos_response = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")

    user = user_response.json()
    todos = todos_response.json()

    done_tasks = [task for task in todos if task.get('completed')]
    total_tasks = todos

    print(f"Employee {user.get('name')} 
          is done with tasks({len(done_tasks)}/{len(todos)}):")

    for task in done_tasks:
        print(f"\t{task.get('title')}")