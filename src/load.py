import pandas as pd
from metadata import DATASETS_FOLDER
import logging

logger = logging.getLogger(__name__)

def load_data(file_name: str) -> pd.DataFrame:
    logger.info(f"Loading {file_name} dataset")
    return pd.read_csv(f"{DATASETS_FOLDER}/{file_name}")
