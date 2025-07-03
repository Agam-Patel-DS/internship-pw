import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from pathlib import Path
from src.mushroomPrediction.exception.exception import CustomException
from src.mushroomPrediction import logger
from src.mushroomPrediction.entity.config_entity import DataTransformationConfig


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        Path(self.config.transformed_dir).mkdir(parents=True, exist_ok=True)

    def read_data(self) -> pd.DataFrame:
        """
        Reads the CSV data from config.raw_data_path
        """
        raw_path = Path(self.config.raw_data_path)
        if not raw_path.exists():
            raise CustomException(f"Raw data file not found at {raw_path}", sys)
        df = pd.read_csv(raw_path)
        logger.info(f"Data read successfully from {raw_path}")
        return df

    def encode_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Applies Label Encoding to all columns
        """
        logger.info("Applying Label Encoding to all categorical features.")
        encoder = LabelEncoder()
        df_encoded = df.apply(encoder.fit_transform)
        return df_encoded

    def split_data(self, df_encoded: pd.DataFrame):
        """
        Splits data into train/test sets
        """
        X = df_encoded.drop("class", axis=1)
        y = df_encoded["class"]
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )
        logger.info("Data split into training and testing sets.")
        return X_train, X_test, y_train, y_test

    def save_transformed_data(self, X_train, X_test, y_train, y_test) -> dict:
        """
        Saves the split datasets as CSV using config file paths
        """
        X_train_path = Path(self.config.X_train_path)
        X_test_path = Path(self.config.X_test_path)
        y_train_path = Path(self.config.y_train_path)
        y_test_path = Path(self.config.y_test_path)

        X_train.to_csv(X_train_path, index=False)
        X_test.to_csv(X_test_path, index=False)
        y_train.to_csv(y_train_path, index=False)
        y_test.to_csv(y_test_path, index=False)

        logger.info("Transformed datasets saved successfully.")
        return {
            "X_train": str(X_train_path),
            "X_test": str(X_test_path),
            "y_train": str(y_train_path),
            "y_test": str(y_test_path),
        }

    def transform_and_save(self) -> dict:
        """
        Orchestrates the full data transformation pipeline
        """
        try:
            df = self.read_data()
            df_encoded = self.encode_features(df)
            X_train, X_test, y_train, y_test = self.split_data(df_encoded)
            paths = self.save_transformed_data(X_train, X_test, y_train, y_test)
            logger.info("Data transformation pipeline completed successfully.")
            return paths
        except Exception as e:
            raise CustomException(e, sys)
