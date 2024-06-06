from typing import List
from sqlalchemy.engine.base import Connection

def generate_dates(start_date: str, end_date: str) -> List[str]: ...

CONN: Connection
DATA_RANGE: List[str]