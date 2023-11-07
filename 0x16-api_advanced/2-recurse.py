#!/usr/bin/python3
"""model that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """send get http req to Reddit API and returns 10 hot posts titels"""

    data = requests.get("https://www.reddit.com/r/{}/hot.json?after={}"
                        .format(subreddit, after),
                        headers={"User-Agent": "My-User-Agent"},
                        allow_redirects=False)
    if data.status_code != 200:
        return None

    titels = data.json()["data"]["children"]
    for title in titels:
        hot_list.append(title.get('data').get('title'))

    the_after = data.json()["data"]["after"]

    if not the_after:
        return hot_list
    else:
        return recurse(subreddit, hot_list, after=the_after)
