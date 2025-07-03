import sys
import joblib
import numpy as np
from src.mushroomPrediction.exception.exception import CustomException
from src.mushroomPrediction import logger
from src.mushroomPrediction.entity.config_entity import PredictionConfig


class Predictor:
    def __init__(self, config: PredictionConfig):
        self.config = config
        self.model = self.load_model()

    def load_model(self):
        try:
            model = joblib.load(self.config.model_path)
            logger.info(f"Loaded model from: {self.config.model_path}")
            return model
        except Exception as e:
            raise CustomException(e, sys)

    def predict(self, input_array: list):
        try:
            input_array = np.array(input_array).reshape(1, -1)
            prediction = self.model.predict(input_array)[0]
            predicted_class = "edible" if prediction == 0 else "poisonous"
            logger.info(f"Prediction: {predicted_class}")
            return predicted_class
        except Exception as e:
            raise CustomException(e, sys)
