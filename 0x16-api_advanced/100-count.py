#!/usr/bin/python3
"""model that queries the Reddit API """
import requests


def count_words(subreddit, word_list, Dict={}, after=None):
    """print hot post base on the programming language"""

    if subreddit is None:
        return None

    data = requests.get("https://www.reddit.com/r/{}/hot.json?after={}"
                        .format(subreddit, after),
                        headers={"User-Agent": "My-User-Agent"},
                        allow_redirects=False)
    if data.status_code != 200:
        return None

    the_after = data.json()["data"]["after"]

    if not the_after:
        Dict = sorted(
            Dict.items(), key=lambda item: (-item[1], item[0].lower()))
        for key, value in Dict:
            print('{}: {}'.format(key, value))
        return
    else:
        post = data.json()["data"]["children"]
        for title in post:
            split_words = title.get('data').get('title').lower().split(' ')
            for word in word_list:
                for word_2 in split_words:
                    word = word.lower()
                    if word == word_2:
                        if word not in Dict:
                            Dict[word] = 0
                        Dict[word] = Dict[word]+1
        return count_words(subreddit, word_list, Dict, after=the_after)
