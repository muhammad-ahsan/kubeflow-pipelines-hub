import yaml
from src.utils import check_dependency
import dask.distributed as dd


def main():
    with open("dependencies.yaml", "r") as file:
        dependencies = yaml.safe_load(file)["dependencies"]

    with dd.Client() as client:
        futures = [client.submit(check_dependency, dependency) for dependency in dependencies]
        results = client.gather(futures)

    success: bool = True
    for dependency, result in zip(dependencies, results):
        print(f"{dependency['name']}: {'OK' if result else 'FAILED'}")
        if not result:
            success = False
    if not success:
        raise Exception("Something requirements are not met")


if __name__ == "__main__":
    main()
