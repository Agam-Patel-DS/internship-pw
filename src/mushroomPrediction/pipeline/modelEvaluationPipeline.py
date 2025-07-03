from src.mushroomPrediction.config.configuration import ConfigurationManager
from src.mushroomPrediction.components.modelEvaluationComponent import ModelEvaluator
from src.mushroomPrediction import logger

def ModelEvaluationPipeline():
        config = ConfigurationManager()
        eval_config = config.ModelEvaluationManager()
        evaluator = ModelEvaluator(eval_config)
        evaluator.evaluate()
