#!/usr/bin/python3
"""
Module to fetch and print the titles of the first 10 hot posts
"""


import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit. If the subreddit is invalid, prints None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 10}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        response.raise_for_status()

        data = response.json()
        if 'data' in data and 'children' in data['data']:
            posts = data['data']['children']
            for post in posts:
                print(post['data']['title'])
        else:
            print("None")
    except requests.exceptions.RequestException:
        print("None")
