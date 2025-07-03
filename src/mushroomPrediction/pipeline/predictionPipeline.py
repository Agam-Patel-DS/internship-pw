from src.mushroomPrediction.config.configuration import ConfigurationManager
from src.mushroomPrediction.components.predictionComponent import Predictor
from src.mushroomPrediction import logger


def PredictionPipeline(input_array: list):
        config = ConfigurationManager()
        prediction_config = config.PredictionManager()
        predictor = Predictor(config=prediction_config)
        prediction = predictor.predict(input_array)
        return prediction
