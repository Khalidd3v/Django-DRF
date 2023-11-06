import requests
import json
api_url = 'http://localhost:8080/api/v1/students_data/'

def get_students_data(id=None):
    params = {}
    if id is not None:
        params['id'] = id

    response = requests.get(url=api_url, params=params)

    if response.status_code == 200:
        data = response.json()
        print(data)
    elif response.status_code == 404:
        error_message = response.json()
        print(error_message.get('error', 'Student not found.'))
    else:
        print(f"Request failed with status code: {response.status_code}")

# Call the function to get the student's data by passing an id parameter to the function
# get_students_data(2)


def create_student_data():
    student_data = {
        'name': 'zakir',
        'roll': 1234555,
        'city': 'gogdara'
    }
    json_data = json.dumps(student_data)
    req = requests.post(url = api_url, data = json_data)
    print(req.status_code)
    print(req.json())

# create_student_data()

def update_student_data():
    student_data = {
        'id': 1,
        'name': 'hamas',
        'roll': 1,
    }
    json_data = json.dumps(student_data)
    req = requests.put(url = api_url, data = json_data)
    print(req.status_code)
    print(req.json())

# update_student_data()


def delete_student_data(id):
    student = {
        'id': id
    }
    json_data = json.dumps(student)
    request = requests.delete(url = api_url, data = json_data)
    print(request.json())

delete_student_data(4)