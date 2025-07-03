import os
from src.mushroomPrediction import logger

def create_directory(destination_path):
  try:
    os.makedirs(destination_path, exist_ok=True)  # exist_ok=True prevents error if directory exists
    logger.info(f"Directory '{destination_path}' created successfully.")
  except OSError as error:
    logger.error(f"Error creating directory '{destination_path}': {error}")

# prompt: function to read yaml from a destinaton path

import yaml
import os

def read_yaml_file(filepath):
  if not os.path.exists(filepath):
    logger.error(f"Error: File not found at {filepath}")
    return None
  try:
    with open(filepath, 'r') as file:
      yaml_data = yaml.safe_load(file)
      return yaml_data
  except yaml.YAMLError as e:
    logger.error(f"Error parsing YAML file: {e}")
    return None
  except Exception as e:
    logger.error(f"An unexpected error occurred: {e}")
    return None