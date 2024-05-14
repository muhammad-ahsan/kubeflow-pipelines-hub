import logging.config
import yaml
from src.utils import check_dependency
import dask.distributed as dd


logging.config.fileConfig('logging_config.ini')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    with open("dependencies.yaml", "r") as file:
        dependencies = yaml.safe_load(file)["dependencies"]

    with dd.Client() as client:
        futures = [client.submit(check_dependency, dependency) for dependency in dependencies]
        results = client.gather(futures)

    success: bool = True
    for dependency, result in zip(dependencies, results):
        logger.info(f"{dependency['name']}: {'OK' if result else 'FAILED'}")
        if not result:
            success = False
    if not success:
        msg = "Pipeline prerequisites failed to satisfy all requirements."
        logger.error(msg)
        raise Exception(msg)


if __name__ == "__main__":
    main()
