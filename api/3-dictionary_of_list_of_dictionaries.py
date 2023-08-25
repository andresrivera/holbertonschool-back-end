#!/usr/bin/python3
"""
-------------------------------------------------------------------------------
MODULE NAME:
-------------------------------------------------------------------------------
    3-dictonary_of_list_of_dictionaries
-------------------------------------------------------------------------------
MODULE DESCRIPTION:
-------------------------------------------------------------------------------
    Using what you did in the task #0, extend your Python script to export data
    in the JSON format.
    REST API: https://jsonplaceholder.typicode.com/
-------------------------------------------------------------------------------
REQUERIMENTS:
-------------------------------------------------------------------------------
    -Records all tasks from all employees
    -Format must be: { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITL
     E", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task":
     "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID": [ {"u
     sername": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_ST
     ATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_CO
     MPLETED_STATUS}, ... ]}
    -File name must be: todo_all_employees.json
-------------------------------------------------------------------------------
IMPORTS:
-------------------------------------------------------------------------------
    -json: That converts a data into a format json
    -requests: for obtain the data that we need from the API
-------------------------------------------------------------------------------
STATUS CODE FOR REQUESTS
-------------------------------------------------------------------------------
    -200 OK: This status code indicates that the request was successful.
    -201 Created: New resource has been successfully created.
    -204 No Content: There is no content to send back in the response.
    -400 Bad Request: Request is malformed or contains invalid parameters.
    -401 Unauthorized: Request lacks valid authentication credentials.
    -403 Forbidden: Similar to 401, but, even if authentication is provided.
    -404 Not Found: The server could not find the requested resource.
    -405 Method Not Allowed: The requested HTTP method is not supported.
    -500 Internal Server Error: This is a generic server error message.
    -502 Bad Gateway: Server acting as a gateway or proxy received.
    -503 Service Unavailable: Server is temporal unable to handle the request.
    -504 Gateway Timeout: Similar to 502, Server acting as a gateway or proxy
         did not receive a timely response from an upstream server.
"""
import json
import requests


if __name__ == "__main__":
    API_URL = "https://jsonplaceholder.typicode.com/"

    response = requests.get("{}todos".format(API_URL),
                            params={"_expand": "user"})

    if response.status_code == 200:
        data = response.json()

        dict_employed = {}

        for task in data:
            dict_employed[task["userId"]] = []

        json_filename = "todo_all_employees.json"
        with open(json_filename, mode="w", encoding="utf-8") as json_file:
            for task in data:
                dict_temp = {
                    "task": task["title"],
                    "completed": task["completed"],
                    "username": task["user"]["username"]
                    }
                dict_employed[task["userId"]].append(dict_temp)

            json.dump(dict_employed, json_file)

    else:
        print("Error: {}".format(response.status_code))
