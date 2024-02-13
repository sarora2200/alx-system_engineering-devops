#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()
        results = response.json().get("data")
        return results.get("subscribers")
    except requests.exceptions.HTTPError as e:
        print(f"Error: {e}")
        return 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py subreddit_name")
        sys.exit(1)
    subreddit_name = sys.argv[1]
    subscribers_count = number_of_subscribers(subreddit_name)
    print(f"Subreddit '{subreddit_name}' has {subscribers_count} subscribers.")
