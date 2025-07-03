import sys
import pandas as pd
import joblib
import mlflow
import mlflow.sklearn

from xgboost import XGBClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from src.mushroomPrediction.exception.exception import CustomException
from src.mushroomPrediction.entity.config_entity import ModelTrainerConfig
from src.mushroomPrediction import logger


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def load_data(self):
        X_train = pd.read_csv(self.config.X_train)
        X_test = pd.read_csv(self.config.X_test)
        y_train = pd.read_csv(self.config.y_train)
        y_test = pd.read_csv(self.config.y_test)
        return X_train, X_test, y_train.values.ravel(), y_test.values.ravel()

    def evaluate(self, model, X_test, y_test):
        y_pred = model.predict(X_test)
        return accuracy_score(y_test, y_pred)

    def train_and_save(self):
        try:
            X_train, X_test, y_train, y_test = self.load_data()

            mlflow.set_experiment("Mushroom_Classification")
            best_score = 0
            best_model = None
            best_model_name = ""

            with mlflow.start_run():
                # RandomForest
                rf_model = RandomForestClassifier(**self.config.RandomForest)
                rf_model.fit(X_train, y_train)
                rf_acc = self.evaluate(rf_model, X_test, y_test)
                mlflow.log_metric("RandomForest_accuracy", rf_acc)
                mlflow.sklearn.log_model(rf_model, "RandomForest")

                if rf_acc > best_score:
                    best_score = rf_acc
                    best_model = rf_model
                    best_model_name = "RandomForest"

                # XGBoost
                xgb_model = XGBClassifier(
                    **self.config.XGBoost,
                    use_label_encoder=False,
                    eval_metric="logloss"
                )
                xgb_model.fit(X_train, y_train)
                xgb_acc = self.evaluate(xgb_model, X_test, y_test)
                mlflow.log_metric("XGBoost_accuracy", xgb_acc)
                mlflow.sklearn.log_model(xgb_model, "XGBoost")

                if xgb_acc > best_score:
                    best_score = xgb_acc
                    best_model = xgb_model
                    best_model_name = "XGBoost"

                # LogisticRegression
                lr_model = LogisticRegression(**self.config.LogisticRegression)
                lr_model.fit(X_train, y_train)
                lr_acc = self.evaluate(lr_model, X_test, y_test)
                mlflow.log_metric("LogisticRegression_accuracy", lr_acc)
                mlflow.sklearn.log_model(lr_model, "LogisticRegression")

                if lr_acc > best_score:
                    best_score = lr_acc
                    best_model = lr_model
                    best_model_name = "LogisticRegression"

                # Save the best model
                joblib.dump(best_model, self.config.model_file)
                mlflow.log_artifact(self.config.model_file)
                logger.info(f"Best model: {best_model_name} with accuracy: {best_score:.4f}")
                logger.info(f"Model saved at: {self.config.model_file}")

        except Exception as e:
            raise CustomException(e, sys)
