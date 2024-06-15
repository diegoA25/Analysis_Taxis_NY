from sqlalchemy import text
import pandas as pd
from generals import CONN

QUERY = """
select vendorid, count(1) as trip_count from nyt.green.taxi_trips
group by vendorid
"""

def query_df():
    try:
        with CONN.connect() as connection:
            result = connection.execute(text(QUERY))
            rows = [(row[0].decode('utf-8', 'ignore'), row[1]) for row in result.fetchall()]
            df = pd.DataFrame(rows, columns=['vendorid', 'trip_count'])
            return df
    except Exception as e:
        print(f"Error executing query: {e}")
        return None

if __name__ == "__main__":
    df = query_df()
    if df is not None:
        print(df)