import requests


def check_internet():
    try:
        requests.get("https://www.google.com", timeout=3)
        return True
    except requests.ConnectionError:
        return False


def check_url(url):
    try:
        requests.get(url, timeout=3)
        return True
    except requests.ConnectionError:
        return False


def check_dependency(dependency):
    if dependency["type"] == "internet":
        return check_internet()
    elif dependency["type"] == "url":
        return check_url(dependency["url"])
