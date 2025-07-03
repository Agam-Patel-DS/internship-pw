from dataclasses import dataclass
@dataclass
class DataIngestionConfig:
    root:str
    raw_data_dir:str
    link:str
    raw_data_name:str


@dataclass
class DataValidationConfig:
    raw_data_path:str
    expected_columns:list
  
@dataclass
class DataTransformationConfig:
    raw_data_path: str                  
    transformed_dir: str                
    X_train_path: str                   
    X_test_path: str                    
    y_train_path: str                   
    y_test_path: str 

@dataclass
class ModelTrainerConfig:
    model_dir: str
    model_file: str
    X_train: str
    X_test: str
    y_train: str
    y_test: str
    RandomForest: dict
    XGBoost: dict
    LogisticRegression: dict


@dataclass
class ModelEvaluationConfig:
    model_path: str
    X_train: str
    y_train: str
    X_test: str
    y_test: str
    report_file: str
