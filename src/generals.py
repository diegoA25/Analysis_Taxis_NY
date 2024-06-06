# General functions for the project

import os
from datetime import datetime
from dateutil.relativedelta import relativedelta
from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv

ENV_PATH = "D:\\Kodigo\\Final Project DAJ\\Analysis_Taxis_NY\\.env"
load_dotenv(ENV_PATH)

def generate_dates(start_date_: str, end_date_: str) -> list:
    start_date_ = datetime.strptime(start_date_, '%Y-%m')
    end_date_ = datetime.strptime(end_date_, '%Y-%m')
    date_list = []
    while start_date_ <= end_date_:
        date_list.append(start_date_date.strftime('%Y-%m'))
        start_date_date += relativedelta(months=1)
    return date_list

POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
DB = "Taxi_ny"

db_string = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{DB}"
CONN = create_engine(db_string)

START_DATE_Q1_ANT = "202001"
END_DATE_Q1_ANT = "202003"

START_DATE_Q1_LAST = "202010"
END_DATE_Q1_LAST = "202012"

START_DATE_Q1_ACT = "202101"
END_DATE_Q1_ACT = "202103"

dates_q1_ant = generate_dates(START_DATE_Q1_ANT, END_DATE_Q1_ANT)
dates_q1_last = generate_dates(START_DATE_Q1_LAST, END_DATE_Q1_LAST)
dates_q1_act = generate_dates(START_DATE_Q1_ACT, END_DATE_Q1_ACT)

DATA_RANGE = dates_q1_ant + dates_q1_last + dates_q1_act

if __name__ == "__main__":
    test_query = "SELECT * FROM green.taxi_trips limit 1"
    print(pd.read_sql(test_query, CONN))
    