#!/usr/bin/python3
"""function that queries the Reddit API and returns
the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """send get http req to Reddit API and returns the number
    of subscribers"""

    data = requests.get("https://www.reddit.com/r/{}/about.json"
                        .format(subreddit),
                        headers={"User-Agent": "badr"},
                        allow_redirects=False)
    if data.status_code > 299:
        return 0
    return data.json()["data"]["subscribers"]
