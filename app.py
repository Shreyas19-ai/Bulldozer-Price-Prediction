import sys
import os
import numpy as np
import pandas as pd

from src.Bulldozer_price_prediction.exception import CustomException
from src.Bulldozer_price_prediction.logger import logging
from src.Bulldozer_price_prediction.components.data_ingestion import DataIngestion

if __name__ == "__main__":
    try:
        data_ingestion = DataIngestion()
        train_data_path , test_data_path,_ = data_ingestion.initiate_data_ingestion()

    except Exception as e:
        raise CustomException(e, sys)