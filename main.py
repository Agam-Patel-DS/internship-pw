from src.mushroomPrediction import logger
from src.mushroomPrediction.exception.exception import CustomException
import sys

logger.info("The Logger is Initialised Here")

import os
from src.mushroomPrediction.pipeline.dataIngestionPipeline import DataIngestionPipeline
from src.mushroomPrediction.pipeline.dataValidationPipeline import DataValidationPipeline
from src.mushroomPrediction.pipeline.dataTransformationPipeline import DataTransformationPipeline
from src.mushroomPrediction.pipeline.modelTrainerPipeline import ModelTrainerPipeline
from src.mushroomPrediction.pipeline.modelEvaluationPipeline import ModelEvaluationPipeline

try:
    DataIngestionPipeline()
except Exception as e:
    logger.error(CustomException(e, sys))

try:
    DataValidationPipeline()
except Exception as e:
    logger.error(CustomException(e, sys))

try:
    DataTransformationPipeline()
except Exception as e:
    logger.error(CustomException(e, sys))

try:
    ModelTrainerPipeline()
except Exception as e:
    logger.error(CustomException(e, sys))

try:
    ModelEvaluationPipeline()
except Exception as e:
    logger.error(CustomException(e, sys))