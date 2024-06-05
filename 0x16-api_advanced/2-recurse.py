#!/usr/bin/python3
"""
Module to recursively fetch and return the titles of all hot posts for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Queries the Reddit API and returns a list containing the titles of all hot articles
    for a given subreddit. If no results are found for the given subreddit, returns None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100}

    if after:
        params['after'] = after

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        response.raise_for_status()

        data = response.json()
        if 'data' in data and 'children' in data['data']:
            posts = data['data']['children']
            hot_list.extend(post['data']['title'] for post in posts)
            after = data['data']['after']
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except requests.exceptions.RequestException:
        return None
