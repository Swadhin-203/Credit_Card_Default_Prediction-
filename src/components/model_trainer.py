import mlflow.sklearn # default sklearn logger for mlflow
from mlflow import log_metric, log_params, log_artifact # specific mlflow logging (optional)
from sklearn.ensemble import RandomForestClassifier  # Model
from sklearn.metrics import accuracy_score  # Scoring
from src.exception import CustomException  # Exception
from src.logger import logging  # Logger
from src.utils import (save_object, read_yaml)  # utility
from dataclasses import dataclass  # dataclass
import os, sys
import warnings

warnings.filterwarnings('ignore')

mlflow.set_tracking_uri('https://dagshub.com/Swadhin-203/Credit_Card_Default_Prediction-.mlflow')


@dataclass(frozen=True)
class ModelTrainerconfig:
    trained_model_file_path = os.path.join('artifacts', 'model.pkl')


class ModelTrainer:
    def __init__(self) -> None:
        self.model_trainer_config = ModelTrainerconfig()
        self.params: dict = read_yaml('PARAMS.yaml')

    def initiate_model_training(self, train_arr, test_arr):
        params = self.params['params']
        log_params(params)
        try:
            mlflow.sklearn.autolog(silent=True)
            logging.info('Splitting Dependent and Independent variables from train and test data')
            X_train, y_train, X_test, y_test = (
                train_arr[:, :-1],
                train_arr[:, -1],
                test_arr[:, :-1],
                test_arr[:, -1]
            )

            logging.info("Random Forest initialized")
            model = RandomForestClassifier(random_state=2)
            model.set_params(**params)  # setting model parameters from params.yaml
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            score = accuracy_score(y_test, y_pred)
            log_metric('accuracy', score)

            logging.info(f"accuracy score of RandomForestClassifier is : {score * 100:.2f}%")

            save_object(

                file_path=self.model_trainer_config.trained_model_file_path,
                obj=model
            )
            # log_artifact(local_path=self.model_trainer_config.trained_model_file_path)
            logging.info("Model training complete and model saved in artifacts as model.pkl")
        except Exception as e:
            raise CustomException(e, sys)
