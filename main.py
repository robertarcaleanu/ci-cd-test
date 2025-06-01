from src.load import load_data
from src.transform import Transformer, balance_dataset
from src.train import train_model
from src.store import store_model
from src.notifier import Notifier
from metadata import MODEL_NAME
import logging

# Global logging configuration
logging.basicConfig(
    level=logging.DEBUG,  # Show all levels
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def main():
    try:
        df = load_data(file_name="bank-full_train_test.csv")
        df = balance_dataset(df)
        df = Transformer().transform(df)
        lr_model = train_model(df=df, target_column="y")
        store_model(model=lr_model, model_name=MODEL_NAME)
    except Exception as e:
        logging.exception(f"An error occurred during the training pipeline. Error: {e}")
        Notifier(process_name="Training Pipeline").print_console_message()


# This allows to run this code only when the main.py file is executed
# It won't be executed when importing it
if __name__ == "__main__":
    main()
