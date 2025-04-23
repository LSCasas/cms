import psycopg
from dotenv import load_dotenv
from config import conn_str

CONN_STRING = conn_str


def select(columns, table, where=None):
    with psycopg.connect(CONN_STRING) as conn:
        with conn.cursor() as cur:
            column_list = ", ".join(columns)
            where_string = f"WHERE {where[0]} {where[1]} {where[2]}" if where else ""
            query = f"SELECT {column_list} FROM {table} {where_string}"
            cur.execute(query)
            result = cur.fetchall()
    return result
