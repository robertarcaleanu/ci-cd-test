import joblib
from datetime import datetime
from metadata import MODELS_FOLDER
import logging

logger = logging.getLogger(__name__)

def store_model(model, model_name: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    model_path = f"{MODELS_FOLDER}/{model_name}_{timestamp}.joblib"
    joblib.dump(model, model_path)
    logger.info(f"Model stored as: {model_path}")
