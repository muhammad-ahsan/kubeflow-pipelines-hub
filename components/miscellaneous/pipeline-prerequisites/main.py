import yaml
import requests
import dask.distributed as dd


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


def main():
    with open("dependencies.yaml", "r") as file:
        dependencies = yaml.safe_load(file)["dependencies"]

    with dd.Client() as client:
        futures = [client.submit(check_dependency, dependency) for dependency in dependencies]
        results = client.gather(futures)

    for dependency, result in zip(dependencies, results):
        print(f"{dependency['name']}: {'OK' if result else 'FAILED'}")


if __name__ == "__main__":
    main()
