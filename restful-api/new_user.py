#!/usr/bin/python3
import requests


url = "http://127.0.0.1:5000/add_user"
data = {
    "username": "Marion",
    "name": "Marion",
    "age": 31,
    "city": "Saint_andré_de_cubzac"
}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=data, headers=headers)
print(response.json())