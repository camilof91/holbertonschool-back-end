#!/usr/bin/python3
"""
Using this REST API, for a given employee ID, returns information about his/her
TODO list progress
"""
import requests
from sys import argv


if __name__ == "__main__":

    employee_id = argv[1]
    filename = f"{employee_id}.json"

    user_response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    )  # .json()
    todos_response = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    )  # .json()

    user = user_response.json()
    todos = todos_response.json()
    done_tasks = [task for task in todos if task.get("completed")]

    with open(filename, "a", newline="") as csv_file:
        for task in todos:
            csv_file.write(f'"{employee_id}",'
                           f'"{user.get("name")}",'
                           f'"{str(task.get("completed"))}",'
                           f'"{task.get("title")}"\n')
