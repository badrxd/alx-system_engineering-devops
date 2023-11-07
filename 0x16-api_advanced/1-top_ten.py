#!/usr/bin/python3
"""model that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit."""
import requests


def top_ten(subreddit):
    """send get http req to Reddit API and returns 10 hot posts titels"""

    data = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                        .format(subreddit),
                        headers={"User-Agent": "badr"},
                        allow_redirects=False)
    if data.status_code > 299:
        print('None')
    else:
        data = data.json()["data"]["children"]
        for title in data:
            print(title['data']['title'])
