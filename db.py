import psycopg
from dotenv import load_dotenv
from config import conn_str

CONN_STRING = conn_str


def select(columns, table, where=None):
    with psycopg.connect(CONN_STRING) as conn:
        with conn.cursor() as cur:
            column_list = ", ".join(columns)
            where_string = ""
            params = []

            if where:
                where_string = f"WHERE {where[0]} {where[1]} %s"
                params.append(where[2])

            query = f"SELECT {column_list} FROM {table} {where_string}"

            cur.execute(query, params)
            result = cur.fetchall()

    return result


def insert(table, columns, values: list):
    with psycopg.connect(CONN_STRING) as conn:
        with conn.cursor() as cur:
            columns = f"({', '.join(columns)})"
            placeholders = ", ".join(["%s"] * len(values))
            query = f"INSERT INTO {table}{columns} VALUES ({placeholders})"
            cur.execute(query, values)
            conn.commit()
