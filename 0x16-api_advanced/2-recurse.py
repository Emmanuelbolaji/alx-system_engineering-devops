#!/usr/bin/python3
"""
Module for recursively querying the Reddit API and returning hot post titles.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): The list to store hot post titles (default is empty).
        after (str): The id of the last post for pagination (default is None).

    Returns:
        list: A list of hot post titles, or None if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
            'User-Agent': 'MyRedditBot/1.0 (by /u/YourUsername)'
            }
    params = {
            'limit': 100,
            'after': after
            }

    try:
        response = requests.get(url, headers=headers, params=params,
                allow_redirects=False)
        if response.status_code != 200:
            return None

        data = response.json()
        posts = data['data']['children']

        for post in posts:
            hot_list.append(post['data']['title'])

        after = data['data']['after']
        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    except Exception:
            return None
