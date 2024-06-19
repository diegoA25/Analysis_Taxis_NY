# General functions for the project

import os
from urllib.parse import quote_plus
from datetime import datetime
from dateutil.relativedelta import relativedelta
from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv

ENV_PATH = ("D:\\Kodigo\\Final Project DAJ\\Analysis_Taxis_NY\\src\\.env")
load_dotenv(ENV_PATH)

def generate_dates(start_date_: str, end_date_: str) -> list:
    start_date_ = datetime.strptime(start_date_, '%Y-%m')
    end_date_ = datetime.strptime(end_date_, '%Y-%m')
    date_list = []
    while start_date_ <= end_date_:
        date_list.append(start_date_.strftime('%Y-%m'))
        start_date_ += relativedelta(months=1)
    return date_list

POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
DB = quote_plus("TaxisNY")

db_string = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{DB}"
CONN = create_engine(db_string)

START_DATE_Q1_ANT = "2020-01"
END_DATE_Q1_ANT = "2020-03"

START_DATE_Q1_LAST = "2020-10"
END_DATE_Q1_LAST = "2020-12"

START_DATE_Q1_ACT = "2021-01"
END_DATE_Q1_ACT = "2021-03"

dates_q1_ant = generate_dates(START_DATE_Q1_ANT, END_DATE_Q1_ANT)
dates_q1_last = generate_dates(START_DATE_Q1_LAST, END_DATE_Q1_LAST)
dates_q1_act = generate_dates(START_DATE_Q1_ACT, END_DATE_Q1_ACT)

DATA_RANGE = dates_q1_ant + dates_q1_last + dates_q1_act

if __name__ == "__main__":
    test_query = "SELECT * FROM nyt.green_taxi_trips limit 1"
    df_test = pd.read_sql(test_query, CONN)
    print(df_test)