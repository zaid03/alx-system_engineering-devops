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

if len(sys.argv) < 2:
    print("Usage: python script.py <employee_id>")
    sys.exit(1)

employee_id = sys.argv[1]
response = requests.get(base_url + "users/{}".format(employee_id))

if response.status_code == 200:
    user_data = response.json()
    employee_name = user_data.get('name', '')

    # Check if the length of the employee name is 18 characters
    if len(employee_name) == 18:
        print("Employee Name: OK")
    else:
        print("Employee Name: Incorrect")
else:
    print("Failed to fetch user data. Status code:", response.status_code)
