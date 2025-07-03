import sys
import pandas as pd
import joblib
from src.mushroomPrediction.entity.config_entity import PredictionConfig
from src.mushroomPrediction.exception.exception import CustomException
from src.mushroomPrediction import logger


class Predictor:
    def __init__(self, config: PredictionConfig):
        self.config = config
        self.model = joblib.load(self.config.model_path)
        self.encoder = joblib.load(self.config.encoder_path)
        logger.info(f"Model and encoder loaded successfully from config paths.")

    def predict(self, input_dict: dict):
        try:
            # Ensure the input dict is converted into a DataFrame with one row
            input_df = pd.DataFrame([input_dict])

            # Encode input using ordinal encoder
            encoded_input = self.encoder.transform(input_df)

            prediction = self.model.predict(encoded_input)[0]
            predicted_class = "edible" if prediction == 0 else "poisonous"
            logger.info(f"Prediction: {predicted_class}")
            return predicted_class

        except Exception as e:
            raise CustomException(f"Prediction failed: {e}", sys)
