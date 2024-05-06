#!/usr/bin/python3
"""
Using this REST API, returns information about all TODO list progress
"""
import requests


if __name__ == "__main__":

    filename = "todo_all_employees.json"
    users_response = requests.get("https://jsonplaceholder.typicode.com/users").json()
    todos_response = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    user_tasks = {}
    for user in users_response:
        user_id = user.get("id")
        username = user.get("username")
        user_tasks[user_id] = []
        for task in todos_response:
            if task.get("userId") == user_id:
                user_tasks[user_id].append({
                    "username": username,
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                })

    with open(filename, "w") as file:
        file.write(str(user_tasks))