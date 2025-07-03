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
  
  