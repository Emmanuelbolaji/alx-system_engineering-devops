#!/usr/bin/env python3
"""
Script to fetch TODO list data for a given employee ID and export to CSV.
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
    username = user_data['username']

    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    return username, todos_data

def export_to_csv(employee_id, username, todos_data):
    """
    Export employee TODO list data to a CSV file.
    """
    filename = f"{employee_id}.csv"

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos_data:
            writer.writerow([
                employee_id,
                username,
                str(todo['completed'])
                todo['title']
                ])


if __name__== "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

    username, todos_data = get_employee_todo_data(employee_id)
    export_to_csv(employee_id, username, todos_data)
    print(f"Data exported to {employee_id}.csv")
