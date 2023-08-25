import sys
import requests

def fetch_employee_todo_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todo_url = f'{base_url}/todos?userId={employee_id}'

    try:
        user_response = requests.get(user_url)
        todo_response = requests.get(todo_url)

        if user_response.status_code == 200 and todo_response.status_code == 200:
            user_data = user_response.json()
            todo_data = todo_response.json()

            employee_name = user_data['name']
            total_tasks = len(todo_data)
            completed_tasks = [task for task in todo_data if task['completed']]
            num_completed_tasks = len(completed_tasks)

            print(f"Employee {employee_name} is done with tasks({num_completed_tasks}/{total_tasks}):")

            for task in completed_tasks:
                print(f"\t{task['title']}")

        else:
            print("Error: Unable to fetch data from the API")

    except requests.exceptions.RequestException as e:
        print("Error:", e)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
    else:
        employee_id = sys.argv[1]
        fetch_employee_todo_progress(employee_id)
