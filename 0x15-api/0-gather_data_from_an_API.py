#!/usr/bin/python3
"""
Returns to-do list information for a given employee ID.

This script takes an employee ID as a command-line argument and fetches
the corresponding user information and to-do list from the JSONPlaceholder API.
It then prints the tasks completed by the employee.
"""

import requests
import sys


# Define the base URL for the API requests
base_url = "https://jsonplaceholder.typicode.com/"

def get_employee_todo_progress(employee_id):
    # Fetch user data
    user_response = requests.get(base_url + "users/{}".format(employee_id))
    if user_response.status_code != 200:
        print("Failed to fetch user data. Status code:", user_response.status_code)
        return

    user_data = user_response.json()
    employee_name = user_data.get('name', 'Unknown')

    # Fetch user's todo list
    todo_response = requests.get(base_url + "todos?userId={}".format(employee_id))
    if todo_response.status_code != 200:
        print("Failed to fetch TODO list data. Status code:", todo_response.status_code)
        return

    todo_data = todo_response.json()
    total_tasks = len(todo_data)
    completed_tasks = [task for task in todo_data if task['completed']]

    # Print employee's todo list progress
    print("Employee {} is done with tasks({}/{}):".format(employee_name, len(completed_tasks), total_tasks))
    for task in completed_tasks:
        print("\t", task['title'])

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
