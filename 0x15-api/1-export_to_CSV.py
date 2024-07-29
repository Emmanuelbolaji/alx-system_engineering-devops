#!/usr/bin/env python3
"""
Script to fetch and display TODO list progress for a given employee ID
using a REST API.
"""

import sys
import csv
import requests


def get_employee_todo_progress(employee_id):
    """
    Fetch and display TODO list progress for the given employee ID.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data['name']

    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo['completed'])

    print(f"Employee {employee_name} is done with "
          f"tasks({completed_tasks}/{total_tasks}):")

    for todo in todos_data:
        if todo['completed']:
            print(f"\t {todo['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
