import os
import sys
import pandas as pd
from pathlib import Path
from src.mushroomPrediction import logger
from src.mushroomPrediction.exception.exception import CustomException
from src.mushroomPrediction.entity.config_entity import DataValidationConfig
from pathlib import Path

class DataValidation:
    def __init__(self, config=DataValidationConfig):
        self.config=config

    def validate_file_exists(self):
        if not Path(self.config.raw_data_path).exists():
            raise CustomException(f"File not found at {self.config.raw_data_path}", sys)
        logger.info(f"Found dataset at {self.config.raw_data_path}")

    def validate_schema(self, df: pd.DataFrame):
        actual_columns = list(df.columns)
        missing_columns = set(self.config.expected_columns) - set(actual_columns)
        extra_columns = set(actual_columns) - set(self.config.expected_columns)

        if missing_columns:
            raise CustomException(f"Missing columns: {missing_columns}", sys)
        if extra_columns:
            logger.warning(f"Unexpected columns found: {extra_columns}")
        logger.info("Column schema validation passed.")

    def validate_nulls(self, df: pd.DataFrame):
        null_counts = df.isnull().sum()
        total_nulls = null_counts.sum()
        if total_nulls > 0:
            logger.warning(f"Found {total_nulls} missing values.")
        else:
            logger.info("No missing values found.")

    def validate_class_balance(self, df: pd.DataFrame):
        class_counts = df["class"].value_counts()
        logger.info(f"Target class distribution:\n{class_counts}")
        if class_counts.min() / class_counts.max() < 0.2:
            logger.warning("Severe class imbalance detected.")

    def run_validation(self):
        try:
            self.validate_file_exists()
            df = pd.read_csv(self.config.raw_data_path)

            self.validate_schema(df)
            self.validate_nulls(df)
            self.validate_class_balance(df)

            logger.info("Data validation Successful")
            return True

        except Exception as e:
            raise CustomException(e, sys)
