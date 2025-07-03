from src.mushroomPrediction import logger
from src.mushroomPrediction.exception.exception import CustomException

logger.info("The Logger is Initialised Here")

import os
from src.mushroomPrediction.pipeline.dataIngestionPipeline import DataIngestionPipeline


try:
    DataIngestionPipeline()
except Exception as e:
    logger.error(CustomException(e, sys))