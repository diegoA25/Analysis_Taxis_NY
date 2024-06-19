# Script to load the clean data into the database
from generals import DATA_RANGE, CONN
import pandas as pd
import os
from tqdm import tqdm

CLEAN_DATA_PATH = "Analysis_Taxis_NY/files_dump/clean_data/"
os.makedirs(CLEAN_DATA_PATH, exist_ok=True) # We create the directory if it doesn't exist
VEH_TYPE = "green_tripdata_"
TABLE_NAME = "green_taxi_trips"


def upload_month(date_: str) -> None:  # This function is used to upload the data for a specific month to the database
    file_name = f"{VEH_TYPE}{date_}.parquet"
    file_path = f"{CLEAN_DATA_PATH}{file_name}"

    df = pd.read_parquet(file_path)
    df.to_sql(
        name=TABLE_NAME,
        con=CONN,
        schema="nyt",
        if_exists="replace",
        index=False
    )

def upload_month_chunks(date_: str, chunk_size_=10000) -> None:
    file_name = f"{VEH_TYPE}{date_}.parquet"
    file_path = f"{CLEAN_DATA_PATH}{file_name}"

    df = pd.read_parquet(file_path)
    total_rows = df.shape[0]
    for i in tqdm(range(0, total_rows, chunk_size_)):
        df_chunk = df[i:i+chunk_size_]  # Chunk Length
        df_chunk.to_sql(
            name=TABLE_NAME,
            con=CONN,
            schema="nyt",
            if_exists="replace",
            index=False
        )

if __name__ == "__main__":
    for date in tqdm(DATA_RANGE):
        upload_month(date)