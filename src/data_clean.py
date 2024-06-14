# Data cleaning Script
import os
import pandas as pd
from tqdm import tqdm
from generals import DATA_RANGE

RAW_DATA_PATH = "/Analysis_Taxis_NY/files_dump/raw_data/"
CLEAN_DATA_PATH = "/Analysis_Taxis_NY/files_dump/clean_data/"
os.makedirs(RAW_DATA_PATH, exist_ok=True)
os.makedirs(CLEAN_DATA_PATH, exist_ok=True)
VEH_TYPE = "green_tripdata_"

# We will create a new column with only the date port of the tpep_pickup_datetime column

def create_data_col(df_: pd.DataFrame) -> pd.DataFrame: # The data frame to modify
    df_["tpep_pickup_date"] = df_["tpep_pickup_datetime"].dt.date
    return df_ # returns the modified data frame

# This will move last column to the 4th position
def order_cols(df_: pd.DataFrame) -> pd.DataFrame: # The data frame to modify
    cols = df_.columns.tolist()
    cols = cols[:2] + cols[-1:] + cols[2:-1]
    df_ = df_[cols]
    df_.columns = df_.columns.str.lower()
    return df_ # Returns the modified Data frame

# Function to clean the data by creating a new column with only the date part and moving the last column to the 4th position
def clean_data(df_: pd.DataFrame) -> pd.DataFrame: # The data frame to modify
    df_ = create_data_col(df_)
    df_ = order_cols(df_)
    for col in df_.columns:
        if df_[col].dtype == 'int32':
            df_[col] = df_[col].astype('int64')
    return df_ # The data frame to modify

# Function to save a data frame to parquet file
def save_clean_data(data_range_: list = DATA_RANGE) -> None: # Data frame to save
    for date in tqdm(data_range_):
        file_name = f"{VEH_TYPE}{date}.parquet"
        df = pd.read_parquet(
            f"{RAW_DATA_PATH}{file_name}"
        )
        df = clean_data(df)
        df.to_parquet(f"{CLEAN_DATA_PATH}{file_name}", index = False)

if __name__ == "__name__":
    save_clean_data()

    