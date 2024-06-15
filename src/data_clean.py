# Data cleaning Script
import pandas as pd
from tqdm import tqdm
from generals import DATA_RANGE

RAW_DATA_PATH = "D:/Kodigo/Final Project DAJ/Analysis_Taxis_NY/files_dump/raw_data/"
CLEAN_DATA_PATH = "D:/Kodigo/Final Project DAJ/Analysis_Taxis_NY/files_dump/clean_data/"
VEH_TYPE = "green_tripdata_"

# We will create a new column with only the date port of the tpep_pickup_datetime column

def create_data_col(df_: pd.DataFrame) -> pd.DataFrame: # The data frame to modify
    if "lpep_pickup_datetime" not in df_.columns:
        raise ValueError("The column 'lpep_pickup_datetime' is not in the DataFrame")
    df_["lpep_pickup_date"] = df_["lpep_pickup_datetime"].dt.date
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

# Function to remove rows with null or zero values
def remove_null_and_zero_rows(df_: pd.DataFrame) -> pd.DataFrame:
    df_ = df_.dropna(how='any') # Drop rows with null values

    for col in df_.columns:
        if df_[col].dtype in ['int64', 'float64']:
            df_ = df_[df_[col] != 0]

    return df_

# Function to save a data frame to parquet file
def save_clean_data(data_range_: list = DATA_RANGE) -> None: # Data frame to save
    for date in tqdm(data_range_):
        file_name = f"{VEH_TYPE}{date}.parquet"
        try:
            df = pd.read_parquet(
                f"{RAW_DATA_PATH}{file_name}"
            )
            print(f"Processing {file_name}...")  # Debugging: indicate the file being processed
            print(f"Columns in {file_name}: {df.columns.tolist()}")  # Debugging: print columns
            
            if "lpep_pickup_datetime" not in df.columns:
                raise ValueError(f"The column 'lpep_pickup_datetime' is not in the DataFrame for {file_name}")

            df = clean_data(df)
            df = remove_null_and_zero_rows(df)
            df.to_parquet(f"{CLEAN_DATA_PATH}{file_name}", index=False)
            print(f"Data for {date} cleaned and saved successfully")
        except Exception as e:
            print(f"Error processing {file_name}: {e}")

if __name__ == "__main__":
    save_clean_data()