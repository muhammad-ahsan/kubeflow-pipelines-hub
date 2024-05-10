import logging

from data_quality import DataQuality

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    data_file = "dataset/iris.csv"

    dq = DataQuality("data-contract/contract.yaml")

    if dq.check_data_quality(data_file):
        logger.info("Data quality check passed!")
    else:
        logger.warning("Data quality check failed")


if __name__ == "__main__":
    main()
