from src.mushroomPrediction.config.configuration import ConfigurationManager
from src.mushroomPrediction.components.modelTrainerComponent import ModelTrainer
from src.mushroomPrediction import logger


def ModelTrainerPipeline():
        config = ConfigurationManager()
        model_trainer_config = config.ModelTrainerManager()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train_and_save()

