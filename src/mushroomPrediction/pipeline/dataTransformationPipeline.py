from src.mushroomPrediction.config.configuration import ConfigurationManager
from src.mushroomPrediction.components.dataTransformationComponent import DataTransformation


def DataTransformationPipeline():
    config = ConfigurationManager()
    data_transformation_config = config.DataTransformationManager()
    data_transformation = DataTransformation(config=data_transformation_config)
    data_transformation.transform_and_save()
