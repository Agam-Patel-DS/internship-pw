import sys
import json
import pandas as pd
import joblib
import mlflow
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from src.mushroomPrediction.exception.exception import CustomException
from src.mushroomPrediction.entity.config_entity import ModelEvaluationConfig
from src.mushroomPrediction import logger


class ModelEvaluator:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def load_model_and_data(self):
        model = joblib.load(self.config.model_path)

        X_train = pd.read_csv(self.config.X_train)
        y_train = pd.read_csv(self.config.y_train)

        X_test = pd.read_csv(self.config.X_test)
        y_test = pd.read_csv(self.config.y_test)

        return model, X_train, y_train.values.ravel(), X_test, y_test.values.ravel()

    def evaluate(self):
        try:
            model, X_train, y_train, X_test, y_test = self.load_model_and_data()

            y_pred_train = model.predict(X_train)
            y_pred_test = model.predict(X_test)

            metrics = {
                "train_accuracy": accuracy_score(y_train, y_pred_train),
                "test_accuracy": accuracy_score(y_test, y_pred_test),
                "test_precision": precision_score(y_test, y_pred_test, average='weighted'),
                "test_recall": recall_score(y_test, y_pred_test, average='weighted'),
                "test_f1": f1_score(y_test, y_pred_test, average='weighted')
            }

            # Save report
            with open(self.config.report_file, "w") as f:
                json.dump(metrics, f, indent=4)

            logger.info(f"Evaluation report saved to {self.config.report_file}")

            # Log to MLflow
            mlflow.set_experiment("Mushroom_Classification")
            with mlflow.start_run():
                mlflow.log_metric("train_accuracy", metrics["train_accuracy"])
                mlflow.log_metric("test_accuracy", metrics["test_accuracy"])
                mlflow.log_metric("test_precision", metrics["test_precision"])
                mlflow.log_metric("test_recall", metrics["test_recall"])
                mlflow.log_metric("test_f1", metrics["test_f1"])
                mlflow.log_artifact(self.config.report_file)

            logger.info("Evaluation metrics logged to MLflow.")

        except Exception as e:
            raise CustomException(e, sys)
