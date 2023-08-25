import requests
from sys import argv

if __name__ == "__main__":
    API_URL = "https://jsonplaceholder.typicode.com/"

    user_id = argv[1]
    response = requests.get("{}users/{}".format(API_URL, user_id),
                            params={"_expand": "todos"})

    if response.status_code == 200:
        user_data = response.json()
        name = user_data["name"]
        tasks = user_data["todos"]
        completed_tasks = [task for task in tasks if task["completed"]]

        print("Employee {} is done with tasks({}/{}):".format(
            name, len(completed_tasks), len(tasks)))

        for task in completed_tasks:
            print("\t{}".format(task["title"]))

    else:
        print("Error: {}".format(response.status_code))
