from src.mushroomPrediction.config.configuration import ConfigurationManager
from src.mushroomPrediction.components.dataValidationComponent import DataValidation


def DataValidationPipeline():
  config=ConfigurationManager()
  data_validation_config=config.DataValidationManager()
  data_validation=DataValidation(config=data_validation_config)
  data_validation.run_validation()