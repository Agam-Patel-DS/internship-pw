import gdown
from src.mushroomPrediction.entity.config_entity import DataIngestionConfig
import os
import kagglehub
import shutil
from pathlib import Path
from src.mushroomPrediction import logger

class DataIngestion:
  def __init__(self,config=DataIngestionConfig):
    self.config=config

  
  def download_data(self):
        if self.config.link:
            file_id = self.config.link.split('/')[-2]
            destination_path = os.path.join(self.config.raw_data_dir, self.config.raw_data_name)
            gdown.download(id=file_id, output=destination_path, quiet=False)
            logger.info(f"Downloaded data to {destination_path}")
            logger.info("Data Ingestion Successfull")
        else:
            logger.warning("No download link provided.")

        