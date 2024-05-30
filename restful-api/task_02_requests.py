#!/usr/bin/python3
import requests
import json


def fetch_and_print_posts():
    """Fetches and prints posts from the API.

    This function sends a GET request to the specified
    API endpoint and retrieves a list of posts.
    It then prints the title of each post.

    Args:
            None

    Returns:
            None
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code: {}".format(response.status_code))
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])
