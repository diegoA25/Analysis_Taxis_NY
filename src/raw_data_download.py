# Phase one file, download data
import os
import logging
import requests
from generals import DATA_RANGE

BASE_LINK = "https://d37ci6vzurychx.cloudfront.net/trip-data/"
VEH_TYPE = "green_tripdata_"
RAW_DATA_PATH = "D:/Kodigo/Final Project DAJ/Analysis_Taxis_NY/files_dump/raw_data/"
os.makedirs(RAW_DATA_PATH, exist_ok=True) # This creates the directory in case it doesn't already exist, if it does then it does nothing

# Logger configuration
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
# Create a console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
# Add handler to logger
logger.addHandler(console_handler)

def get_data_month(date_: str) -> None:
    url = f"{BASE_LINK}{VEH_TYPE}{date_}.parquet"
    file_name = f"{VEH_TYPE}{date_}.parquet"
    path = os.path.join(RAW_DATA_PATH, file_name)

    # Download the file
    try:
        with requests.get(url, stream=True, timeout=30) as r:
            if r.status_code == 200:
                with open(path, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=1024**2):
                        f.write(chunk)
                logger.info("File %s successfully downloaded", file_name)
                
                # Verify file integrity (optional but recommended)
                if os.path.getsize(path) == 0:
                    os.remove(path)
                    logger.error("Downloaded file %s is empty. Removed the file.", file_name)
                else:
                    logger.info("File %s passed integrity check.", file_name)
            else:
                if os.path.exists(path):
                    os.remove(path)
                logger.error("Failed to download the file %s: HTTP status code %d", file_name, r.status_code)
                r.raise_for_status()
    except requests.exceptions.RequestException as e:
        logger.error("Request failed for %s: %s", file_name, e)
        if os.path.exists(path):
            os.remove(path)

def get_data_range(data_range: list = DATA_RANGE) -> None:
    for date in data_range:
        if os.path.exists(os.path.join(RAW_DATA_PATH, f"{VEH_TYPE}{date}.parquet")):
            logger.info("File %s already exists", f"{VEH_TYPE}{date}.parquet")
        else:
            get_data_month(date)

if __name__ == "__main__":
    get_data_range()