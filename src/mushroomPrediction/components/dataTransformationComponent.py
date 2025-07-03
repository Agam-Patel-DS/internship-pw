import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder, LabelEncoder
from pathlib import Path
from src.mushroomPrediction.exception.exception import CustomException
from src.mushroomPrediction import logger
from src.mushroomPrediction.entity.config_entity import DataTransformationConfig
import joblib


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        Path(self.config.transformed_dir).mkdir(parents=True, exist_ok=True)

    def read_data(self) -> pd.DataFrame:
        raw_path = Path(self.config.raw_data_path)
        if not raw_path.exists():
            raise CustomException(f"Raw data file not found at {raw_path}", sys)
        df = pd.read_csv(raw_path)
        logger.info(f"Data read successfully from {raw_path}")
        return df

    def encode_features(self, df: pd.DataFrame) -> pd.DataFrame:
        logger.info("Applying encoding to features and target.")
        
        # Split features and target
        feature_df = df.drop(columns=["class"])
        target_series = df["class"]

        # Encode features
        ordinal_encoder = OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1)
        X_encoded = ordinal_encoder.fit_transform(feature_df)
        X_df = pd.DataFrame(X_encoded, columns=feature_df.columns)

        # Encode target
        label_encoder = LabelEncoder()
        y_encoded = label_encoder.fit_transform(target_series)
        X_df["class"] = y_encoded

        # Save encoders
        encoder_dir = Path("artifacts/encoders")
        encoder_dir.mkdir(parents=True, exist_ok=True)
        joblib.dump(ordinal_encoder, encoder_dir / "ordinal_encoder.pkl")
        joblib.dump(label_encoder, encoder_dir / "label_encoder_y.pkl")
        logger.info("Encoders saved successfully.")

        return X_df

    def split_data(self, df_encoded: pd.DataFrame):
        X = df_encoded.drop("class", axis=1)
        y = df_encoded["class"]
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )
        logger.info("Data split into training and testing sets.")
        return X_train, X_test, y_train, y_test

    def save_transformed_data(self, X_train, X_test, y_train, y_test) -> dict:
        X_train.to_csv(self.config.X_train_path, index=False)
        X_test.to_csv(self.config.X_test_path, index=False)
        y_train.to_csv(self.config.y_train_path, index=False)
        y_test.to_csv(self.config.y_test_path, index=False)
        logger.info("Transformed datasets saved successfully.")
        return {
            "X_train": str(self.config.X_train_path),
            "X_test": str(self.config.X_test_path),
            "y_train": str(self.config.y_train_path),
            "y_test": str(self.config.y_test_path),
        }

    def transform_and_save(self) -> dict:
        try:
            df = self.read_data()
            df_encoded = self.encode_features(df)
            X_train, X_test, y_train, y_test = self.split_data(df_encoded)
            paths = self.save_transformed_data(X_train, X_test, y_train, y_test)
            logger.info("Data transformation pipeline completed successfully.")
            return paths
        except Exception as e:
            raise CustomException(e, sys)
