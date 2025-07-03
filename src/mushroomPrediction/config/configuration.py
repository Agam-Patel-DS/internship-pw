from src.mushroomPrediction.utils.common import read_yaml_file, create_directory
from src.mushroomPrediction.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig, ModelEvaluationConfig
from pathlib import Path

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
  
  def DataValidationManager(self):
    config=self.config["data_validation"]
    data_validation_config=DataValidationConfig(
        raw_data_path=config["raw_data_path"],
        expected_columns=config["expected_columns"]
    )
    return data_validation_config

  def DataTransformationManager(self):
    config = self.config["data_transformation"]
    create_directory(config["processed_data_dir"])
    data_transformation_config = DataTransformationConfig(
        raw_data_path = config["raw_data_path"],
        transformed_dir = config["processed_data_dir"],
        X_train_path = config["X_train_path"],
        X_test_path = config["X_test_path"],
        y_train_path = config["y_train_path"],
        y_test_path = config["y_test_path"]
    )

    return data_transformation_config

  def ModelTrainerManager(self):
    config=self.config["model_training"]
    params=self.params
    create_directory(config["model_dir"])
    model_training_config=ModelTrainerConfig(
        model_dir=config["model_dir"],
        model_file=config["model_file"],
        X_train=config["X_train"],
        X_test=config["X_test"],
        y_train=config["y_train"],
        y_test=config["y_test"],
        RandomForest=params["RandomForest"],
        XGBoost=params["XGBoost"],
        LogisticRegression=params["LogisticRegression"]
        )
    return model_training_config

  def ModelEvaluationManager(self) -> ModelEvaluationConfig:
        config = self.config["model_evaluation"]
        create_directory(Path(config["report_file"]).parent)

        model_evaluation_config= ModelEvaluationConfig(
            model_path=config["model_path"],
            X_train=config["X_train"],
            y_train=config["y_train"],
            X_test=config["X_test"],
            y_test=config["y_test"],
            report_file=config["report_file"]
        )
        return model_evaluation_config