import logging
import os
from pathlib import Path
from typing import Union

import yaml
import pandas as pd


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DataQuality:
    def __init__(self, data_contract_file: Union[str, Path]):

        if not os.path.isfile(data_contract_file):
            raise FileNotFoundError(data_contract_file)

        self.data_contract_file = data_contract_file
        self.data_contract = self.__read_data_contract()

    def __read_data_contract(self):
        with open(self.data_contract_file, 'r') as file:
            data_contract_yaml = yaml.safe_load(file)
        return data_contract_yaml

    def check_data_quality(self, data_file) -> bool:
        if not os.path.isfile(data_file):
            raise FileNotFoundError(data_file)

        df = pd.read_csv(data_file)

        missing_columns = set(self.data_contract["required_columns"]) - set(df.columns)
        if missing_columns:
            logger.warning("Missing columns:", missing_columns)
            return False

        for column, expected_type in self.data_contract["data_types"].items():
            if df[column].dtype != expected_type:
                logger.warning(
                    f"Invalid dataset type for column {column}. Expected: {expected_type}, Found: {df[column].dtype}")
                return False

        missing_values_ratio = df.isnull().mean()
        if missing_values_ratio.max() > self.data_contract["missing_values_threshold"]:
            logger.warning("Too many missing values")
            return False

        # All checks passed
        logger.info("Data quality check passed!")
        return True



