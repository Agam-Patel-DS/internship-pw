from src.mushroomPrediction.utils.common import read_yaml_file, create_directory
from src.mushroomPrediction.entity.config_entity import DataIngestionConfig, DataTransformationConfig, ModelTrainingConfig, PredictionConfig

class ConfigurationManager:
  def __init__(self):
    self.config=read_yaml_file("config/config.yaml")
    self.params=read_yaml_file("params.yaml")
    create_directory(self.config["root"])

  def DataIngestionManager(self):
    config=self.config["data_ingestion"]
    create_directory(config["raw_data_dir"])
    data_ingestion_config=DataIngestionConfig(
        root=config["root"],
        raw_data_dir=config["raw_data_dir"],
        link=config["link"],
        raw_data_name=config["raw_data_name"]
    )
    return data_ingestion_config

  def DataTransformationManager(self):
    config=self.config["data_transformation"]
    create_directory(config["processed_data_dir"])
    data_transformation_config=DataTransformationConfig(
        
    )
    return data_transformation_config

  def ModelTrainingManager(self):
    config=self.config["model_training"]
    params=self.params
    create_directory(config["root"])
    create_directory(config["model_dir"])
    model_training_config=ModelTrainingConfig(
        
        
    )
    return model_training_config

  def PredictionManager(self):
    config=self.config["prediction"]
    prediction_config=PredictionConfig(
      
      
    )
    return prediction_config