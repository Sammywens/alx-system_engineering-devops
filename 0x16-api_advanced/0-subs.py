#!/usr/bin/python3
""" Write a function that queries the Reddit API and returns the
number of subscribers (not active users, total subscribers) for a
given subreddit. If an invalid subreddit is given, the function
should return 0. """
import requests


def number_of_subscribers(subreddit):
        url = f"https://www.reddit.com/r/{subreddit}/about.json"
        headers = {"User-Agent": "Python/requests"}
        try:
            response = requests.get(url, headers=headers, allow_redirects=False)
            response.raise_for_status()  # Raise an exception for HTTP errors (e.g., 404, 500)
            data = response.json()
            subscribers = data.get("data", {}).get("subscribers", 0)  # Default to 0 if data or subscribers key is missing
            return subscribers
        except requests.HTTPError as e:
            print(f"HTTP Error: {e}")
            return 0
        except requests.RequestException as e:
            print(f"Request Exception: {e}")
            return 0
        except ValueError as e:
            print(f"ValueError: {e}")
            return 0
