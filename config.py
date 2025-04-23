import psycopg
from dotenv import load_dotenv
import os

load_dotenv()
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

conn_str = f"dbname = {DB_NAME} user = {DB_USER} host = {DB_HOST} port = {DB_PORT}"

with psycopg.connect(conn_str) as connection:
    print("successful connection")
