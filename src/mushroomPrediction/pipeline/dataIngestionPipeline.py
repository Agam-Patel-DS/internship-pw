from src.mushroomPrediction.config.configuration import ConfigurationManager
from src.mushroomPrediction.components.dataIngestionComponent import DataIngestion


def DataIngestionPipeline():
  config=ConfigurationManager()
  data_ingestion_config=config.DataIngestionManager()
  data_ingestion=DataIngestion(config=data_ingestion_config)
  data_ingestion.download_data()