import sys
import os
from src.Bulldozer_price_prediction.exception import CustomException
from src.Bulldozer_price_prediction.logger import logging
import pandas as pd
import numpy as np
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    raw_data_path: str = os.path.join("artifacts", "data.csv")
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")
    valid_data_path: str = os.path.join("artifacts", "valid.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data Ingestion started")
        try:
            # ingesting/reading the data from the source
            train_path = pd.read_csv("notebooks/Train.csv", low_memory=False)
            test_path = pd.read_csv("notebooks/Test.csv")
            valid_path = pd.read_csv("notebooks/Valid.csv")

            logging.info("Data has been read")

            # making the directory to save the data
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)

            # saving the ingested data to the artifacts folder
            train_path.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_path.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            valid_path.to_csv(self.ingestion_config.valid_data_path, index=False, header=True)

            logging.info("Data ingestion has completed")

            # returning the paths where data is saved
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
                self.ingestion_config.valid_data_path
            )

        except Exception as e:
            raise CustomException(e, sys)