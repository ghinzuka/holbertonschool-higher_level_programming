#!/usr/bin/python3
import requests
import json
import csv


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


def fetch_and_save_posts():
    """
    Fetches posts from the JSONPlaceholder API and saves them to a CSV file.

    This function sends a GET request to the JSONPlaceholder
    API to retrieve a list of posts.
    It then converts the response to JSON format and extracts
    the necessary data (id, title, body) from each post.
    The extracted data is then written to a CSV file
    named 'posts.csv' with the headers 'id', 'title', and 'body'.

    Returns:
            None
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        posts = response.json()
        posts_data = []
        for post in posts:
            post_dict = {
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            }
            posts_data.append(post_dict)

        with open('posts.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(posts_data)
